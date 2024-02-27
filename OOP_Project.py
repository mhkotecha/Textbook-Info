package Project;

class Course
{
    String courseName;
    Instructor Instructor;
    TextBook textBook;
    Course(String name,Instructor instr,TextBook text)
    {
        courseName=name;
        Instructor=instr;
        textBook=text;
    }
    public String getName()
    {
        return courseName;
    }
    public Instructor getInstructor()
    {
        return Instructor;
    }
    public TextBook getTextBook()
    {
        return textBook;
    }
    @Override
    public String toString()
    {
        return "CourseName: "+courseName+"\n"+Instructor.toString()+"\n"+textBook.toString();
    }
}
class Instructor
{
    String firstName;
    String lastName;
    String officeNumber;
    Instructor(String lname,String fname,String office)
    {
        firstName=fname;
        lastName=lname;
        officeNumber=office;
    }
    Instructor(Instructor object2)
    {
        firstName=object2.firstName;
        lastName=object2.lastName;
        officeNumber=object2.officeNumber;
    }
    public void set(String lname,String fname,String office)
    {
        firstName=fname;
        lastName=lname;
        officeNumber=office;
    }
    @Override
    public String toString()
    {
        return "Instructor Information:\nLast Name: "+lastName+"\nFirst Name: "+firstName+"\nOffice Number: "+officeNumber;
    }
}
class TextBook
{
    String title;
    String author;
    String publisher;
    TextBook(String title,String author,String publisher)
    {
        this.title=title;
        this.author=author;
        this.publisher=publisher;
    }
    TextBook(TextBook object2)
    {
       this.title=object2.title;
        this.author=object2.author;
        this.publisher=object2.publisher;
    }
    public void set(String title,String author,String publisher)
    {
        this.title=title;
        this.author=author;
        this.publisher=publisher;
    }
    public String toString()
    {
        return "TextBook Information:\nTitle: "+title+"\nAuthor: "+author+"\nPublisher: "+publisher;
    }
}
public class Project1{

     public static void main(String []args){
         // Create an Instructor object
        Instructor myInstructor = new Instructor("Wallace", "Mike", "XYZ 123");
        //Create a Textbook object
        TextBook myTextBook = new TextBook("How to not write a Program", "Steve Jobs", "Apple");
        //Create a Course object
        Course myCourse = new Course("Computer Science", myInstructor, myTextBook);
        //Display the course information
        System.out.println(myCourse);
     }
}
