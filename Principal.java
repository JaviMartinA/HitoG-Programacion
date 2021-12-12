package com.ejemplo;

public class Principal {

	public static void main(String[] args) {
		Empleado empleado1=new Empleado("Ivan", 30000, "Programador");
		Hijo hijo1=new Hijo();
		String mensaje=hijo1.comer("McDonalds");
		System.out.println(mensaje);
		System.out.println(empleado1.Ficha());
		Persona[] comida={hijo1,empleado1};
		comida[1].comer("Goiko");
		String polimorfismo=comida[1].comer("Goiko");
		System.out.println(polimorfismo);

	}

}//cierra clase
