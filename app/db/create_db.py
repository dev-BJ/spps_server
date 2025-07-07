import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    user="root",
    password="root"
)

conn.autocommit = True  # Enable autocommit mode

cur = conn.cursor()
cur.execute("CREATE DATABASE spps_db;")
# cur.execute("USE spps_db;")

# cur.execute("""
#             INSERT INTO public.users (first_name,last_name,email,gender,date_of_birth,user_id,"password",department,"role") VALUES
# 	 ('John','Doe','test@gmail.com','male','12/07/1664','john.doe','1234567','COmputer Science','lecturer'),
# 	 ('James','Bond','test@gmail.com','male','12/07/1664','15h/0001/cs','1234567','Computer Science','student');
#             """)
# cur.execute("""
#             INSERT INTO public.courses (course_code,course_title,lecturer_id) VALUES
# 	 ('STA 429','Statistics',2),
# 	 ('COM 101','Intro to Computer',2),
# 	 ('MTH 101','Into to Math',2),
# 	 ('GNS 101','Citizenship Education',2);
#             """)
# cur.execute("""
#             INSERT INTO public.student_offered_courses (user_id,course_id,semester,"session") VALUES
# 	 (1,1,'1st','20/21'),
# 	 (1,2,'1st','20/21'),
# 	 (1,3,'1st','20/21'),
# 	 (1,4,'1st','20/21'),
# 	 (1,1,'1st','20/21'),
# 	 (1,2,'1st','20/21'),
# 	 (1,3,'1st','20/21'),
# 	 (1,4,'1st','20/21');
#             """)

cur.close()
conn.close()