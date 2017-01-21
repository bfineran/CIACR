
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLConnection;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;


public class CIAcrawler {

	private String baseurl = 
			"https://www.cia.gov/library/readingroom/collection/general-cia-records?page=1";
	private HttpURLConnection httpConnection;

	public CIAcrawler() throws IOException{
		FileWriter f = new FileWriter("DocPDFLinks.txt");
		BufferedWriter b = new BufferedWriter(f);

		for (int i = 1; i <= 38438; i++) {
			scrapePage(i, b);
			System.out.println(i);
		}
		
		System.out.println("Done");
		b.close();
		f.close();
	}
	
	public void scrapePage(int pagenum, BufferedWriter b) throws IOException{
		//open a connection
		try {
			URL url = new URL(baseurl + pagenum);

			URLConnection connection = url.openConnection();
			httpConnection = (HttpURLConnection) connection;

		} catch (Exception e) {
			e.printStackTrace();
		}
		//printStatusCode();
		
		//put the html contents into document object
		ArrayList<String> contents = getContents();
		StringBuilder page = new StringBuilder();
		for (String c : contents) {
			page.append(c);
		}
		Document doc = Jsoup.parse(page.toString());
		
		//scrape document object for pdf links and write them
		Elements links = doc.getElementsByAttributeValueStarting("type", "application/pdf");
		for (Element n : links) {
			b.write(n.attr("href") + "\n");
		}
	}
	/**
	 * This method will print the status codes from the connection.
	 */
	public void printStatusCode() {

		try {

			int code = httpConnection.getResponseCode();
			String message = httpConnection.getResponseMessage();

			System.out.println(code + " : " + message);
		} catch (Exception e) {
			e.printStackTrace();
		}

	}

	/**
	 * This method will get the HTML contents.
	 * 
	 * @return the array list of contents of the page.
	 */
	@SuppressWarnings("resource")
	public ArrayList<String> getContents() {

		ArrayList<String> contents = new ArrayList<String>();
		Scanner in;
		try {
			in = new Scanner(httpConnection.getInputStream());

			while (in.hasNextLine()) {
				String line = in.nextLine();
				contents.add(line);
			}
		} catch (Exception e) {
			e.printStackTrace();
		}

		return contents;

	}
	
	@SuppressWarnings("resource")
	public static String getDoc(HttpURLConnection huc){
		StringBuilder s = new StringBuilder();
		Scanner in;
		try {
			in = new Scanner(huc.getInputStream());

			while (in.hasNextLine()) {
				String line = in.nextLine();
				s.append(line);
			}
		} catch (Exception e) {
			e.printStackTrace();
		}
		return s.toString();
		
	}

	public static void main(String[] args) {
		try {
			CIAcrawler a = new CIAcrawler();
		} catch (IOException e) {e.printStackTrace();}
	}
}
