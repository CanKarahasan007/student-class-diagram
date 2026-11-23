# Student Class Diagram

```mermaid
classDiagram
    class Address {
        +str street
        +str city
        +str postal_code
        +__str__() str
    }

    class Person {
        +str name
        +str email
        +Address address
    }

    class Professor {
        +str staff_id
    }

    class Student {
        +str student_id
        +dict grades
        +enroll(course)
        +set_grade(course, grade)
        +get_average() float
    }

    class Course {
        +str code
        +str title
        +Professor professor
        +list students
        +add_student(student)
    }

    Person <|-- Professor : inherits
    Person <|-- Student : inherits
    Person "1" --> "1" Address : has
    Professor "1" --> "0..*" Course : teaches
    Student "0..*" --> "0..*" Course : enrolls in
