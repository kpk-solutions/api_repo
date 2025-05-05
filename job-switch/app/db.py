import sqlite3

def save_to_db(job_data):
    conn = sqlite3.connect('job_data.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS jobs (title TEXT, company TEXT)''')
    for job in job_data:
        cursor.execute("INSERT INTO jobs (title, company) VALUES (?, ?)", (job['title'], job['company']))
    conn.commit()
    conn.close()
