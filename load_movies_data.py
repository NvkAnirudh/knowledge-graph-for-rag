from dotenv import load_dotenv
load_dotenv()

import os
from langchain_community.graphs import Neo4jGraph

NEO4J_URI = os.getenv('NEO4J_URI')
NEO4J_USERNAME = os.getenv('NEO4J_USERNAME')
NEO4J_PASSWORD = os.getenv('NEO4J_PASSWORD')
NEO4J_DATABASE = os.getenv('NEO4J_DATABASE')

print("Connecting to Neo4j...")
kg = Neo4jGraph(url=NEO4J_URI, username=NEO4J_USERNAME, password=NEO4J_PASSWORD, database=NEO4J_DATABASE)

# Load the classic Movies dataset (same as Neo4j's sample)
print("Loading Movies dataset...")

cypher_load = """
// Create Movies
CREATE (TheMatrix:Movie {title:'The Matrix', released:1999, tagline:'Welcome to the Real World'})
CREATE (Keanu:Person {name:'Keanu Reeves', born:1964})
CREATE (Carrie:Person {name:'Carrie-Anne Moss', born:1967})
CREATE (Laurence:Person {name:'Laurence Fishburne', born:1961})
CREATE (Hugo:Person {name:'Hugo Weaving', born:1960})
CREATE (LillyW:Person {name:'Lilly Wachowski', born:1967})
CREATE (LanaW:Person {name:'Lana Wachowski', born:1965})
CREATE (JoelS:Person {name:'Joel Silver', born:1952})

CREATE (Keanu)-[:ACTED_IN {roles:['Neo']}]->(TheMatrix)
CREATE (Carrie)-[:ACTED_IN {roles:['Trinity']}]->(TheMatrix)
CREATE (Laurence)-[:ACTED_IN {roles:['Morpheus']}]->(TheMatrix)
CREATE (Hugo)-[:ACTED_IN {roles:['Agent Smith']}]->(TheMatrix)
CREATE (LillyW)-[:DIRECTED]->(TheMatrix)
CREATE (LanaW)-[:DIRECTED]->(TheMatrix)
CREATE (JoelS)-[:PRODUCED]->(TheMatrix)

CREATE (TheMatrixReloaded:Movie {title:'The Matrix Reloaded', released:2003, tagline:'Free your mind'})
CREATE (Keanu)-[:ACTED_IN {roles:['Neo']}]->(TheMatrixReloaded)
CREATE (Carrie)-[:ACTED_IN {roles:['Trinity']}]->(TheMatrixReloaded)
CREATE (Laurence)-[:ACTED_IN {roles:['Morpheus']}]->(TheMatrixReloaded)
CREATE (Hugo)-[:ACTED_IN {roles:['Agent Smith']}]->(TheMatrixReloaded)
CREATE (LillyW)-[:DIRECTED]->(TheMatrixReloaded)
CREATE (LanaW)-[:DIRECTED]->(TheMatrixReloaded)
CREATE (JoelS)-[:PRODUCED]->(TheMatrixReloaded)

CREATE (TheMatrixRevolutions:Movie {title:'The Matrix Revolutions', released:2003, tagline:'Everything that has a beginning has an end'})
CREATE (Keanu)-[:ACTED_IN {roles:['Neo']}]->(TheMatrixRevolutions)
CREATE (Carrie)-[:ACTED_IN {roles:['Trinity']}]->(TheMatrixRevolutions)
CREATE (Laurence)-[:ACTED_IN {roles:['Morpheus']}]->(TheMatrixRevolutions)
CREATE (Hugo)-[:ACTED_IN {roles:['Agent Smith']}]->(TheMatrixRevolutions)
CREATE (LillyW)-[:DIRECTED]->(TheMatrixRevolutions)
CREATE (LanaW)-[:DIRECTED]->(TheMatrixRevolutions)
CREATE (JoelS)-[:PRODUCED]->(TheMatrixRevolutions)

CREATE (TheDevilsAdvocate:Movie {title:"The Devil's Advocate", released:1997, tagline:'Evil has its winning ways'})
CREATE (Charlize:Person {name:'Charlize Theron', born:1975})
CREATE (Al:Person {name:'Al Pacino', born:1940})
CREATE (Taylor:Person {name:'Taylor Hackford', born:1944})
CREATE (Keanu)-[:ACTED_IN {roles:['Kevin Lomax']}]->(TheDevilsAdvocate)
CREATE (Charlize)-[:ACTED_IN {roles:['Mary Ann Lomax']}]->(TheDevilsAdvocate)
CREATE (Al)-[:ACTED_IN {roles:['John Milton']}]->(TheDevilsAdvocate)
CREATE (Taylor)-[:DIRECTED]->(TheDevilsAdvocate)

CREATE (AFewGoodMen:Movie {title:"A Few Good Men", released:1992, tagline:"In the heart of the nation's capital, in a courthouse of the U.S. government, one man will stop at nothing to keep his honor, and one will stop at nothing to find the truth."})
CREATE (TomC:Person {name:'Tom Cruise', born:1962})
CREATE (JackN:Person {name:'Jack Nicholson', born:1937})
CREATE (DemiM:Person {name:'Demi Moore', born:1962})
CREATE (KevinB:Person {name:'Kevin Bacon', born:1958})
CREATE (KieferS:Person {name:'Kiefer Sutherland', born:1966})
CREATE (NoahW:Person {name:'Noah Wyle', born:1971})
CREATE (CubaG:Person {name:'Cuba Gooding Jr.', born:1968})
CREATE (KevinP:Person {name:'Kevin Pollak', born:1957})
CREATE (JTW:Person {name:'J.T. Walsh', born:1943})
CREATE (JamesM:Person {name:'James Marshall', born:1967})
CREATE (ChristopherG:Person {name:'Christopher Guest', born:1948})
CREATE (RobR:Person {name:'Rob Reiner', born:1947})
CREATE (AaronS:Person {name:'Aaron Sorkin', born:1961})

CREATE (TomC)-[:ACTED_IN {roles:['Lt. Daniel Kaffee']}]->(AFewGoodMen)
CREATE (JackN)-[:ACTED_IN {roles:['Col. Nathan R. Jessup']}]->(AFewGoodMen)
CREATE (DemiM)-[:ACTED_IN {roles:['Lt. Cdr. JoAnne Galloway']}]->(AFewGoodMen)
CREATE (KevinB)-[:ACTED_IN {roles:['Capt. Jack Ross']}]->(AFewGoodMen)
CREATE (KieferS)-[:ACTED_IN {roles:['Lt. Jonathan Kendrick']}]->(AFewGoodMen)
CREATE (NoahW)-[:ACTED_IN {roles:['Cpl. Jeffrey Barnes']}]->(AFewGoodMen)
CREATE (CubaG)-[:ACTED_IN {roles:['Cpl. Carl Hammaker']}]->(AFewGoodMen)
CREATE (KevinP)-[:ACTED_IN {roles:['Lt. Sam Weinberg']}]->(AFewGoodMen)
CREATE (JTW)-[:ACTED_IN {roles:['Lt. Col. Matthew Andrew Markinson']}]->(AFewGoodMen)
CREATE (JamesM)-[:ACTED_IN {roles:['Pfc. Louden Downey']}]->(AFewGoodMen)
CREATE (ChristopherG)-[:ACTED_IN {roles:['Dr. Stone']}]->(AFewGoodMen)
CREATE (AaronS)-[:ACTED_IN {roles:['Man in Bar']}]->(AFewGoodMen)
CREATE (RobR)-[:DIRECTED]->(AFewGoodMen)
CREATE (AaronS)-[:WROTE]->(AFewGoodMen)

CREATE (TopGun:Movie {title:"Top Gun", released:1986, tagline:'I feel the need, the need for speed.'})
CREATE (KellyM:Person {name:'Kelly McGillis', born:1957})
CREATE (ValK:Person {name:'Val Kilmer', born:1959})
CREATE (AnthonyE:Person {name:'Anthony Edwards', born:1962})
CREATE (TomS:Person {name:'Tom Skerritt', born:1933})
CREATE (MegR:Person {name:'Meg Ryan', born:1961})
CREATE (TonyS:Person {name:'Tony Scott', born:1944})
CREATE (JimC:Person {name:'Jim Cash', born:1941})

CREATE (TomC)-[:ACTED_IN {roles:['Maverick']}]->(TopGun)
CREATE (KellyM)-[:ACTED_IN {roles:['Charlie']}]->(TopGun)
CREATE (ValK)-[:ACTED_IN {roles:['Iceman']}]->(TopGun)
CREATE (AnthonyE)-[:ACTED_IN {roles:['Goose']}]->(TopGun)
CREATE (TomS)-[:ACTED_IN {roles:['Viper']}]->(TopGun)
CREATE (MegR)-[:ACTED_IN {roles:['Carole']}]->(TopGun)
CREATE (TonyS)-[:DIRECTED]->(TopGun)
CREATE (JimC)-[:WROTE]->(TopGun)

CREATE (JerryMaguire:Movie {title:'Jerry Maguire', released:2000, tagline:'The rest of his life begins now.'})
CREATE (ReneeZ:Person {name:'Renee Zellweger', born:1969})
CREATE (KellyP:Person {name:'Kelly Preston', born:1962})
CREATE (JerryO:Person {name:"Jerry O'Connell", born:1974})
CREATE (JayM:Person {name:'Jay Mohr', born:1970})
CREATE (BonnieH:Person {name:'Bonnie Hunt', born:1961})
CREATE (ReginaK:Person {name:'Regina King', born:1971})
CREATE (JonathanL:Person {name:'Jonathan Lipnicki', born:1996})
CREATE (CameronC:Person {name:'Cameron Crowe', born:1957})

CREATE (TomC)-[:ACTED_IN {roles:['Jerry Maguire']}]->(JerryMaguire)
CREATE (CubaG)-[:ACTED_IN {roles:['Rod Tidwell']}]->(JerryMaguire)
CREATE (ReneeZ)-[:ACTED_IN {roles:['Dorothy Boyd']}]->(JerryMaguire)
CREATE (KellyP)-[:ACTED_IN {roles:['Avery Bishop']}]->(JerryMaguire)
CREATE (JerryO)-[:ACTED_IN {roles:['Frank Cushman']}]->(JerryMaguire)
CREATE (JayM)-[:ACTED_IN {roles:['Bob Sugar']}]->(JerryMaguire)
CREATE (BonnieH)-[:ACTED_IN {roles:['Laurel Boyd']}]->(JerryMaguire)
CREATE (ReginaK)-[:ACTED_IN {roles:['Marcee Tidwell']}]->(JerryMaguire)
CREATE (JonathanL)-[:ACTED_IN {roles:['Ray Boyd']}]->(JerryMaguire)
CREATE (CameronC)-[:DIRECTED]->(JerryMaguire)
CREATE (CameronC)-[:PRODUCED]->(JerryMaguire)
CREATE (CameronC)-[:WROTE]->(JerryMaguire)
"""

try:
    kg.query(cypher_load)
    print("✓ Data loaded successfully!")

    # Verify the data
    result = kg.query("MATCH (n) RETURN count(n) as count")
    print(f"✓ Total nodes in database: {result[0]['count']}")

    # Show breakdown by type
    result = kg.query("MATCH (n) RETURN DISTINCT labels(n) as labels, count(*) as count")
    print("\nNode breakdown:")
    for row in result:
        print(f"  {row['labels']}: {row['count']} nodes")

except Exception as e:
    print(f"Error: {e}")
