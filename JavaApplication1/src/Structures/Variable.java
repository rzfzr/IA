package Structures;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author rzfzr
 */
public class Variable {
    
    private boolean objective;
    private String identification;
    private String name;    
    private String type;
    private Object temp;
    
    
    public Variable(boolean objective,
            String indentification,
            String name,
            String type){
        
        this.objective=objective;
        this.identification=indentification;
        this.name=name;
        this.type=type;
        
    }
//    private 
//    private WorkMemory workmemory;


}
