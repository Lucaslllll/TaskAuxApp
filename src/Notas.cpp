#include "Notas.hpp"

using namespace std;

Notas::Notas(std::string nome, std::string data, Pessoa *p){
        m_nome = nome;
        m_data = data;
        m_autor = p;
};

void Notas::set_status(bool status){
    m_status = status;
};

bool Notas::get_status(){
    return m_status;
};


string Notas::get_nome(){
    return m_nome;
};


string Notas::get_detalhes(){
    return m_detalhes;
};
	

Pessoa* Notas::get_autor(){
    return *m_autor;
};
