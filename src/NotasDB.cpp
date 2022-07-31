#include "NotasDB.hpp"


using namespace std;

NotasDB::NotasDB(){
    
};

// salvar em m_notas e em algum db sql
void NotasDB::salvar(Notas *nota){
    m_notas.push_back(nota);
    string caminho = "../data/notas criadas/"+nota->get_nome()+".txt";
    
    ofstream file(caminho, ios::trunc);
    file << nota->get_detalhes();
    file << "\n\n\n\n" << "Autor da Nota: " << nota->get_autor()->get_nome() << ", Data da Nota: " << nota->get_data() << ", Terminou: " << nota->get_status();
    
    
};
void NotasDB::deletar(Notas *nota){
    
};
