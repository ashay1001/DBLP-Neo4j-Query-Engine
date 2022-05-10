# from neo4j import GraphDatabase
import logging
import os

from flask import (
    Flask,
    g,
    jsonify,
    request,
    Response,
    render_template
)
from neo4j import (
    GraphDatabase,
    basic_auth,
)

app = Flask(__name__, template_folder='templates', static_url_path='/static')

url = os.getenv("NEO4J_URI", "bolt://localhost:7687")
username = os.getenv("NEO4J_USER", "neo4j")
password = os.getenv("NEO4J_PASSWORD", "Articles_with_Authors")
neo4j_version = os.getenv("NEO4J_VERSION", "4")
database = os.getenv("NEO4J_DATABASE", "neo4j")

port = os.getenv("PORT", 8080)

# driver = GraphDatabase.driver(uri = "bolt://localhost:7687", auth = ("neo4j", "password"))
driver = GraphDatabase.driver(uri = url, auth =basic_auth(username, password))
session = driver.session()

# text = "EBG"

# q2 = ("""

# CALL db.index.fulltext.queryNodes("articlesAll", $param)
# YIELD node, score
# with node.title as titles, score
# unwind titles as title
# match (n:Article)<-[:AUTHOR]-(p) where n.title = title
# return n.title as Article, p.name as Author, score as Score, p.degree_wb_authors/100 as Relevance 
# order by Score,Relevance desc limit $lmt

# """)

def get_db():
    if not hasattr(g, "neo4j_db"):
        if neo4j_version.startswith("4"):
            g.neo4j_db = driver.session(database=database)
        else:
            g.neo4j_db = driver.session()
    return g.neo4j_db


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, "neo4j_db"):
        g.neo4j_db.close()

# def get_records():
#     records = session.run(q2, param = text)
#     # records = session.run(q1)
#     print(records)
#     for data in records:
#         print(data)
#     return records


def serialize_records_1(record):
    return {
            "title": record["Article"],
            "author": record["Author"],
            "score": record["Score"],
            "relevance": record["Relevance"],
            }

def serialize_records_2(record):
    return {
            "author": record["Author"],
            "page_rank": record["Page_Rank"],
            }

def serialize_records_3(record):
    return {
            "title": record["title"],
            "author": record["author"],
            "own_rel": record["own_r"],
            "other_author": record["other_auth"],
            "other_author_rel": record["other_auth_relevance"],
            }

@app.route("/")
def get_index():
    return render_template('index.html',
                        header='Header 1', 
                        sub_header='Input Query', 
                        list_header="Query Response",
                        # records=get_records(), 
                        # records=get_search(),
                        site_title="Article Query Engine"
                        )
    # return app.send_static_file("index.html")


@app.route("/search")
def get_search():
    def work(tx, query, lmt = 10):
        return list(tx.run(
            "CALL db.index.fulltext.queryNodes(\"articlesAll\", $param) "
            "YIELD node, score "
            "with node.title as titles, score "
            "unwind titles as title "
            "match (n:Article)<-[:AUTHOR]-(p) where n.title = title "
            "return n.title as Article, p.name as Author, score as Score, p.degree_wb_authors/100 as Relevance "
            "order by Score desc limit $lmt ",
            {"param": query, "lmt": int(lmt)}
        ))


    try:
        q = request.args["q"]
        lmt = request.args["lmt"]
        # q = request.args[0]
        # lmt = request.args[1]
        print(q, lmt)
    except KeyError:
        return []
    else:
        db = get_db()
        results = db.read_transaction(work, q, int(lmt))
        # print(results[0]["n.title"])
        records = [serialize_records_1(record) for record in results]

        return jsonify(records)

@app.route("/keyword")
def get_keyword():
    return render_template('keyword.html',
                        header='Header 1', 
                        sub_header='Input Query', 
                        list_header="Query Response",
                        # records=get_records(), 
                        # records=get_search(),
                        site_title="Article Query Engine"
                        )

@app.route("/findPageRank")
def get_findPR():
    return render_template('findPR.html',
                        header='Header 1', 
                        sub_header='Input Query', 
                        list_header="Query Response",
                        # records=get_records(), 
                        # records=get_search(),
                        site_title="Article Query Engine"
                        )


@app.route("/findPR")
def get_search2():
    def work(tx, query, lmt = 10):
        return list(tx.run(
            "CALL db.index.fulltext.queryNodes(\"articlesAll\", $param) "
            "yield node with collect(node.authors) as authors unwind authors as author "
            "unwind author as name "
            "match (n)-[:WRITTEN_BY]-(m:Author) where m.name=name "
            "return distinct m.name as Author, m.pgrank_wb_authors as Page_Rank order by Page_Rank desc limit $lmt",
            {"param": query, "lmt": int(lmt)}
        ))


    try:
        q = request.args["q"]
        lmt = request.args["lmt"]
        # print(q, lmt)
    except KeyError:
        return []
    else:
        db = get_db()
        results = db.read_transaction(work, q, int(lmt))
        records = [serialize_records_2(record) for record in results]
        # print(records)
        return jsonify(records)



@app.route("/calcProf")
def get_calcProf():
    return render_template('calcProf.html',
                        header='Header 1', 
                        sub_header='Input Query', 
                        list_header="Query Response",
                        # records=get_records(), 
                        # records=get_search(),
                        site_title="Article Query Engine"
                        )


@app.route("/calcProfiling")
def get_search3():
    def work(tx, query, lmt = 10):
        return list(tx.run(
            "match (n:Article)-[:WRITTEN_BY]-(m:Author) where m.name= $param "
            "with collect(n.title)as titles unwind titles as title "
            "match (n:Author)-[r:COAUTHOR]-(m:Author) where n.name= $param "
            "and r.title = title return title, n.name as author, n.degree_wb_authors/100 as own_r, " 
            "m.name as other_auth, m.degree_wb_authors/100 as other_auth_relevance limit $lmt ",
            {"param": query, "lmt": int(lmt)}
        ))


    try:
        q = request.args["q"]
        lmt = request.args["lmt"]
        # print("*"*40,q, lmt)
    except KeyError:
        return []
    else:
        db = get_db()
        results = db.read_transaction(work, q, int(lmt))
        records = [serialize_records_3(record) for record in results]
        # print(records)
        return jsonify(records)

@app.route("/about")
def get_about():
    return render_template('about.html',
                        header='Header 1', 
                        sub_header='Input Query', 
                        list_header="Query Response",
                        # records=get_records(), 
                        records=get_search(),
                        site_title="Article Query Engine"
                        )

if __name__ == "__main__":
    logging.root.setLevel(logging.INFO)
    logging.info("Starting on port %d, database is at %s", port, url)
    app.run(port=port, debug=True)