import pandas as pd
from app.data.db import connect_database


def InsertDataset(id, name, category, fileSize):
    """Insert new incident."""
    conn = connect_database()
    cursor = conn.cursor()
    cursor.execute(f"""
        INSERT INTO Datasets_Metadata 
        (id, dataset_name, category, file_size_mb)
        VALUES (?, ?, ?, ?)
    """, (id, name, category, fileSize))
    
    conn.commit()
    incident_id = cursor.lastrowid
    conn.close()
    return incident_id


def GetAllDatasets(filter: str):
    """
        Get all Datasets as DataFrame.
    """
    conn = connect_database()
    df = pd.read_sql_query(f"SELECT * FROM Datasets_Metadata WHERE {filter}", conn)
    conn.close()
    
    return df


def UpdateDatasets(id: str, newId: str, name: str, ctgry: str, newSize :str):
    conn = connect_database()
    cursor = conn.cursor()
    cursor.execute(f"""UPDATE Cyber_Incidents
                    SET id = ?, dataset_name = ?, category = ?, file_size_mb = ?
                    WHERE id = ?""", (int(newId), name, ctgry, float(newSize), int(id)))
    conn.commit()
    conn.close()


def DeleteDataset(id: str):
    conn = connect_database()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Datasets_Metadata WHERE id = ?", (int(id), ))
    conn.commit()
    conn.close()


def TransferCSV():
    import csv
    from pathlib import Path
    conn = connect_database()
    cursor = conn.cursor()
    with open(Path("Week 08/DATA/Datasets_Metadata.csv").resolve()) as itFile:
        reader = csv.reader(itFile)
        header: bool = True
        for row in reader:
            if header == True:
                header = False
                continue
            cursor.execute("INSERT INTO Datasets_Metadata (id, dataset_name, category, file_size_mb) VALUES (?, ?, ?, ?)", (int(row[0]), row[1], row[2], row[3]))

    conn.commit()
    conn.close()