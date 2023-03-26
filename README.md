# DBLP-Neo4j-query-engine

### DBLP Query Engine using Neo4j graphDB. 

### Dataset:-
- The DBLP server provides bibliographic information of Scholarly Data on major computer science journals and proceedings.
- Dataset:- [Citation Network Dataset: DBLP+Citation, ACM Citation network](https://www.aminer.org/citation) DBLP-Citation-network V10

### Architecture:-
![Architecture](/arch/arch1.PNG "Architecture")

- Operations:
    - Keyword Discovery
    - Researcher Profiling
    - Influencing Author


### Setup Application
- Install Neo4j Desktop or any Neo4j DB instance. Download the DBLP dataset, and import it in Neo4j DB.

- Run required Cypher scripts.

### Add queries sections required for initial setup.

- Download this git repo.
```
git clone https://github.com/ashay1001/DBLP-Neo4j-Query-Engine.git
```

- Create a virtual env for this app in python.
```
pip install virtualenv

python -m venv DBLP-Neo4j-query-engine

.\DBLP-Neo4j-query-engine\Scripts\activate

pip install -r requirements.txt
```

- Launch Flask web app.
```
python app.py
```
