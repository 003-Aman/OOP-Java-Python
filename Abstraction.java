/* show the user what is important and hide what is not
 * 
*/
abstract class Animal{// this is just an abstract a concept so we cannot make an object out of it
    
    Animal(){// this is a constructor please keep in mind
        System.out.println("You are creating a new animal");
    }
    abstract void walk();// what we did here is created an abstract class and function
    // which means that all the other classes which inherit this class should have the walk method but doesnt need anything from this class itself
    public void eat(){
        System.out.println("Animal eats");
    }
}
class Horse extends Animal{
    Horse(){//this is also a constructor
        System.out.println("You created a horse");
    }
    public void walk(){
        System.out.println("walks on two legs");
    }
}
class Chicken extends Animal{
    public void walk(){
        System.out.println("walks on four legs");
    }
}


public class Abstraction {
    public static void main(String[] args) {
        Horse horse = new Horse();// both the constructors are called
        horse.walk();
        horse.eat();
    }
    
}
