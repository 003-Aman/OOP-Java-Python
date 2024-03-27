/*
single level inheritance: one classes attributes and functions are used by another but with different values
multi level inheritance : grandpa to father to son
heirarchial inheritance: one to many
hyprid : one to many but one specific son can have his own child, basically can be single, multi, and heirarchial all at once
multiple inheritance : in java we use interfaces to use this but in other it is used normally like C++
 */



class Shape{
    public void area(){
        System.out.println("Area Displayed");
    }
}
class Rectangle extends Shape{

    public void area(int l,int b){
        System.out.println(l*b);
    }
}

class Square extends Rectangle{
    public void area(int l, int b){
        System.out.println(l*b);
    }

class Circle extends Shape{
    public void area(int r){
        System.out.println(3.14*r*r);
    }
}
}



public class TypesOfInheritance {
    public static void main(String[] args) {
        
    }
    
}
