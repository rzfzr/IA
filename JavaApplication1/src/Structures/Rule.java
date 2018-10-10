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
public class Rule {
    
    private String id;
    
    public Variable var0;
    public Variable var1;
    
    
    
    
    public Antecedent antecedent;
    public Consequent consequent;
    
    public Rule(String id, Antecedent antecedent, Consequent consequent){
        this.id=id;
        this.antecedent=antecedent;
        this.consequent=consequent;
        
    }
    
    
}
