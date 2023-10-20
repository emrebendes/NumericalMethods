package hatalar;

public class Demo {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		System.out.println("tamsayýlarda yuvarlama hatasý örneði");
		byte b = 127;
		System.out.println(b);
		System.out.println(++b);
		System.out.println(++b);
		System.out.println("tamsayýlarda yuvarlama hatasý örnekleri");
		float s1=0,f= 0.00001f,f2=0.00000999999974737875163555145263671875f;
		float f3 =1_000_000_001f , f4= 1_000_000_000f;
		if (f3==f4)
			System.out.println("aaaa");
		double d3 = 1_000_000_001 , d4= 1_000_000_000;
		if (d3==d4)
			System.out.println("bbbbb");
		double s2=0,d= 0.00001,d2=1,s3=0;
		for (long i=0;i<1000000;i++) {
			s1+=f;
			s2+=d;
			s3+=d2;
		}
	
		System.out.println(s1);
		System.out.println(s2);
		System.out.println(s3);
		
		float[] ss1 = dis(1f,3000.001f,3f);
		double[] ss2 = dis(1,3000.001,3);
		System.out.println(ss1[0]+"-"+ss1[1]);
		System.out.println(ss2[0]+"-"+ss2[1]);
		float[] ss3 = dis2(1f,3000.001f,3f);
		double[] ss4 = dis2(1,3000.001,3);
		System.out.println(ss3[0]+"-"+ss3[1]);
		System.out.println(ss4[0]+"-"+ss4[1]);
	}
	
	public static float[] dis(float a,float b,float c) {
		float x1 = (-b + (float)Math.sqrt(b*b-4*a*c))/(2*a) ;
		float x2 = (-b - (float)Math.sqrt(b*b-4*a*c))/(2*a) ;
		float[] s ={x1,x2};
		return s;
	}
	public static double[] dis(double a,double b,double c) {
		double x1 = (-b + Math.sqrt(b*b-4*a*c))/(2*a) ;
		double x2 = (-b - Math.sqrt(b*b-4*a*c))/(2*a) ;
		double[] s ={x1,x2};
		return s;
	}
	public static float[] dis2(float a,float b,float c) {
		float x1 = (-2*c)/(b + (float)Math.sqrt(b*b-4*a*c))  ;
		float x2 = (-2*c)/(b - (float)Math.sqrt(b*b-4*a*c)) ;
		float[] s ={x1,x2};
		return s;
	}
	public static double[] dis2(double a,double b,double c) {
		double x1 = (-2*c)/(b + Math.sqrt(b*b-4*a*c)) ;
		double x2 = (-2*c)/(b - Math.sqrt(b*b-4*a*c)) ;
		double[] s ={x1,x2};
		return s;
	}
	

}
