public class Polyporphism {
    //poly morphism = many forms
    //function overloading and function overriding = compile time polymorphism and run time polymorphism

    //FUNCTION OVERLOADING: functions which do different work but have the same name, which is what were going to discuss here
    //compile time polymorphism
    public static void main(String[] args) {
        Phone phone = new Phone();
        phone.company = "Apple";
        
        phone.year = 2015;

        phone.displayInfo(phone.company);
        phone.displayInfo(phone.year);

        
    }
    
}

class Phone{
    String company;
    int year;//we cannot have two functions which use the same datatype,but it didnt work


    public void displayInfo(String company){System.out.println(this.company);}
    
        
    public void displayInfo(int year){System.out.println(this.year);}


}
