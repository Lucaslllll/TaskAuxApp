#include "Pessoa.hpp"

using namespace std;

Pessoa::Pessoa(string nome){
    m_nome = nome;
};

string Pessoa::get_nome(){
    return m_nome;
}
