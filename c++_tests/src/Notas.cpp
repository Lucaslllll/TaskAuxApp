#include "Notas.hpp"

using namespace std;

Notas::Notas(std::string nome, std::string data, Pessoa *p){
        m_nome = nome;
        m_data = data;
        m_autor = p;
};

string Notas::get_data(){
        return m_data;
};

void Notas::set_status(bool status){
    m_status = status;
};

string Notas::get_status(){
    if (m_status == 0) // bool em c++ é 0 ou 1
        return "Não";
    return "Sim";
};


string Notas::get_nome(){
    return m_nome;
};


void Notas::add_detalhes(string detalhes){
    m_detalhes.append(detalhes);
};

string Notas::get_detalhes(){
    return m_detalhes;
};
	

Pessoa* Notas::get_autor(){
    return m_autor;
};
