//Find Author
match (n:Article)<-[:AUTHOR]-(p) where n.title = 'A Heterogeneous System for Real-Time Detection with AdaBoost' return n.title,p.name