classroom = [
    {
        'name': 'Alice',
        'email': 'alice@example.com',
        'grades': [
            ('math', 91),
            ('english', 78),
            ('math', 90),
            ('history', 34),
            ('math', 95),
        ],
    },
    {
        'name': 'Bob',
        'email': 'bob@example.com',
        'grades': [
            ('math', 85),
            ('english', 92),
            ('history', 75),
        ],
    },
    {
        'name': 'Charlie',
        'email': 'charlie@example.com',
        'grades': [
            ('physics', 78),
            ('english', 81),
            ('english', 89),
            ('history', 68),
            ('english', 82),
            ('physics', 91),
        ],
    },
]
def add_student(name, email=None):
     if(email==None):
       namelower=name.lower()
       email=f'{namelower}@example.com'
       s={'name': name,
          'email':email,
          'grades':[]  
      }
     else:
          s={   
          'name': name,
          'email':email,
          'grades':[] 
           }
     classroom.append(s)

def return_index(name):
    count=0
    for student in classroom:
        if(student['name']==name): 
          return count
        count+=1
    return -1

def delete_student(name):
   if(return_index(name)!=-1):
            index=return_index(name)
            del classroom[index]

def set_email(name, email):
    index=return_index(name)
    classroom[index]['email']=email

def add_grade(name, profession, grade):
    index=return_index(name)
    if(index!=-1):
      t=(profession,grade)
      classroom[index]['grades'].append(t)

def avg_grade(name, profession):
     index=return_index(name)
     if(index!=-1):
          count=0
          sum_all=0
          for  grade in classroom[index]['grades']:
            if grade[0]==profession:
               count+=1
               sum_all+=grade[1]
          return (sum_all/count)

def get_professions(name):
      index=return_index(name)
      if(index!=-1):
         l=[]
         for i in classroom[index]['grades']:
            if(l.__contains__(i[0])==False):
                l.append(i[0])
         return l

