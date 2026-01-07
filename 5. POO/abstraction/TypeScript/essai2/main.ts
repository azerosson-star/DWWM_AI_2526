abstract class Person {
    abstract name: string;

    display(): void {
        const element = document.getElementById("resultat");
        if (element) {
          element.textContent = `Name: ${this.name}`; // Use textContent for cleaner output
        } else {
          console.error("Element with id 'resultat' not found.");
        }
    }
}

class Employee extends Person { 
    name: string;
    empCode: number;
    
    constructor(name: string, code: number) { 
        super(); // must call super()
        
        this.empCode = code;
        this.name = name;
    }
}

let emp: Person = new Employee("Patrick", 100);
emp.display(); //James