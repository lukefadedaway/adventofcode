import java.io.*;
import java.net.URISyntaxException;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class solution {

	 public static void main(String[] args) throws URISyntaxException, IOException {
		 String[] towers = new String[9];
		 String[] towers2 = new String[9];
		 File jarFile = new File(solution.class.getProtectionDomain().getCodeSource().getLocation().toURI().getPath());
		 String inputFilePath = jarFile.getParent() + File.separator + "Day 5" + File.separator + args[0]; 
		 Pattern p = Pattern.compile("\\d+");
		 Matcher m;
		    
		 File file = new File(inputFilePath);
		 BufferedReader br = new BufferedReader(new FileReader(file));
		  
		 for(int i=0;i<9;i++) {
			 towers[i] = "";
			 towers2[i] = "";
		 }
		 
		 String s;
		 while ((s = br.readLine()).trim().startsWith("[")) {
			 s += " ";
			 for(int i = 0; i<= s.length()-4; i+=4) {
				 char c = s.substring(i,i+4).charAt(1);
				 if(c != ' ') {
					 towers[i/4] += c;
					 towers2[i/4] += c;
				 }
			 }
		 }
		 
		 s = br.readLine();
		 
		 int moveNum, moveFrom, moveTo;
//		 for(String st: towers) {
//			 System.out.println(st);
//		 }
		 
		 StringBuffer sbr;
		 
		 while((s = br.readLine()) != null) {
			 m = p.matcher(s);
			 m.find();
			 moveNum = Integer.parseInt(m.group());
			 m.find();
			 moveFrom = Integer.parseInt(m.group()) - 1;
			 m.find();
			 moveTo = Integer.parseInt(m.group()) - 1;
//			 System.out.println("Move " + moveNum + " from " + moveFrom + " to " + moveTo);
			 sbr = new StringBuffer(towers[moveFrom].subSequence(0, moveNum));
			 sbr.reverse();
			 towers[moveTo] = sbr.toString() + towers[moveTo];
			 towers[moveFrom] = towers[moveFrom].substring(moveNum);
			 towers2[moveTo] = towers2[moveFrom].subSequence(0, moveNum) + towers2[moveTo];
			 towers2[moveFrom] = towers2[moveFrom].substring(moveNum);
//			 for(String st: towers) {
//				 System.out.println(st);
//			 }
		 }
		 
//		 for(String st: towers) {
//			 System.out.println(st);
//		 }
		 
		 System.out.println("Part 1:");
		 for(String st: towers) {
			 try {
				System.out.print(st.charAt(0));
			} catch (Exception e) {
				System.out.print(" ");
			}
		 }
		 System.out.println();
		 System.out.println("Part 2:");
		 for(String st: towers2) {
			 try {
				System.out.print(st.charAt(0));
			} catch (Exception e) {
				System.out.print(" ");
			}
		 }
		 System.out.println();
	 }	
}
