package com.pankajvma.springdemo.mvc;

import javax.servlet.http.HttpServletRequest;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
@RequestMapping("/hello")
public class HelloWorldController {
	
	// need a controller method to show the initial HTML form
	@RequestMapping("/showForm")
	public String showWebForm(){
		return "helloworld-form";
	}
	
	// need a controller method to process the HTML form
	@RequestMapping("/processForm")
	public String processWebForm(){
		return "helloworld";
	}
	
	//new controller method to read form data
	// add data to the model
	@RequestMapping("/processFormVersion2")
	public String letsShoutDude(HttpServletRequest request, Model model) {
		
		// read the request parameter from the HTML form
		String theName = request.getParameter("studentName");
		
		// convert the data to all caps
		theName = theName.toUpperCase();
		
		// create the Strings
		String result = "Yo! " + theName;
		String result2 = "Your name has " + theName.length() + " characters.";
		
		// add an attribute named "message" to the model, assign it the value of result. This value can be accessed on the view page with the help of attribute's name
		model.addAttribute("message", result);
		model.addAttribute("charCount", result2);
		
		// return name of view page
		return "helloworld";
	}
	
	//new controller method to read form data with the help of annotations, it will provide same output as the above method
	// add data to the model
	@RequestMapping("/processFormVersion3")
	public String letsShoutDude(@RequestParam("studentName") String theName, Model model) {
	
		// convert the data to all caps
		theName = theName.toUpperCase();
			
		// create the Strings
		String result = "Yo! " + theName;
		String result2 = "Your name has " + theName.length() + " characters. This form is being generated  with V3 method code that uses annotations.";
			
		// add an attribute named "message" to the model, assign it the value of result. This value can be accessed on the view page with the help of attribute's name
		model.addAttribute("message", result);
		model.addAttribute("charCount", result2);
			
		// return name of view page
		return "helloworld";
	}
}
