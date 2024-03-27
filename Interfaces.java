interface Animal{//watch the video well to understand its properties and way it works
    void walk(); // cannot make another function due to proper abstraction

}
interface Herbivore{}

class Horse implements Animal, Herbivore{
    public void walk(){
        System.out.println("walks on 4 legs");
    }
}


public class Interfaces {//proper abstraction and cannot take constructors
    
}
