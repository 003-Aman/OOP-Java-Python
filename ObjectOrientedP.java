//OBSERVE THE CODE CAREFULLY

class Pen{
    String color;
    String type; //gel or bp

    public void write(){
        System.out.println("Wrote something.");
    }

    public void printColor(){

        System.out.println(this.color);
    }
    

}

class Student{
    String name;
    int age;

    public void printInfo(){
        System.out.println(this.name);
        System.out.println(this.age);
    }
}





public class ObjectOrientedP{
    public static void main(String[] args) {
        Pen pen1 = new Pen(); // remember object is created this way in java
        pen1.color = "Red";
        pen1.type = "Gel";

        pen1.write();

        Pen pen2 = new Pen();
        pen2.color = "Black";
        pen2.type = "Ballpoint";

        pen1.printColor();
        pen2.printColor();


        Student s1 = new Student();
        s1.name = "Aman";
        s1.age = 20;

        Student s2 = new Student();
        s2.name = "Piyush";
        s2.age = 22;

        s1.printInfo();
        s2.printInfo();
    }

}