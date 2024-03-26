class Student{
    String name;// this is the most confusing part when we create classes in java because this is not a constructor
    int age;
     String college;
    
    //the problem is every is needed at the beginning of the class, everything is needed which is used in the code
    


    // Student(){ // here is the main funda of constructors can be parameterized
    //     //which means that while creating an object you have to give two paremeters at that instance, this is basic man cmon
    //     System.out.println("Constructor called");//this is what is under the def __init__ in python
    //     //can be given like this.stack =[], all that stuff that is to be done when object is created
    // }

    Student(String name, int age){
        this.name = name;
        this.age = age;
        this.college = "Augustana";
    }
}




public class OOP2 {
    public static void main(String[] args) {
        
    }
    
}
