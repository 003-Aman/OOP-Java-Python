public class OOPS{
    public static void main(String[] args) {

        Coding c1= new Coding("Aman Shrestha","ML and AI");
        c1.display_resume();

        
    }
}

class Coding{
    String year;
    String skill;

    Coding(String year, String skill){
        this.year = year;
        this.skill = skill;
    }

    void display_resume(){
        System.out.println(this.year +" , "+ this.skill);
    }
}