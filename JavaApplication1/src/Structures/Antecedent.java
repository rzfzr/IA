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
public class Antecedent {


    private Variable variable;
    private String operacao;
    private String valor;
    private String conectivo;
    
    public Antecedent(Variable variable, String operacao, String valor, String conectivo) throws Exception {
        this.variable = variable;
        if(variable.equals("n")) {
            if(operacao == "=" || operacao == "<>" || operacao == ">" || operacao == "<" || operacao == "<=" || operacao == ">=") {
                this.operacao = operacao;
            }
            else {
                throw new Exception("Operação inválida!");
            }
        }
        else {
            if(operacao == "=" || operacao == "<>") {
                this.operacao = operacao;
            }
            else {
                throw new Exception("Operação inválida!");
            }
        }
//        
//        for(int i = 0; i < variable.getValores().size(); i++) {
//            if(variavel.getValores().get(i) == valor) {
//                this.valor = valor;
//                break;
//            }
//        }
        if(this.valor == null) {
            throw new Exception("Valor inválido!");
        }
        if(conectivo == "E" || conectivo == "OU") {
            this.conectivo = conectivo;
        }
        else {
            throw new Exception("Conectivo inválido!");
        }
    }

    public String getOperacao() {
        return operacao;
    }

    public void setOperacao(String operacao) {
        this.operacao = operacao;
    }

    public String getValor() {
        return valor;
    }

    public void setValor(String valor) {
        this.valor = valor;
    }

    public String getConectivo() {
        return conectivo;
    }

    public void setConectivo(String conectivo) {
        this.conectivo = conectivo;
    }
    
    
}
