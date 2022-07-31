#ifndef Notas_hpp
#define Notas_hpp

#include <iostream>
#include <vector>
#include <sstream>
#include <algorithm>

#include "Pessoa.hpp"

class Notas{


private:
	std::string m_nome;
	std::string m_detalhes;
	std::string m_data;
	bool m_status = false;
	Pessoa *m_autor;

public:
	Notas(std::string nome, std::string m_data, Pessoa *p);

    std::string get_data();
    void set_status(bool status);
	std::string get_status();
	std::string get_nome();
    void add_detalhes(std::string detalhes);
    std::string get_detalhes();
	Pessoa* get_autor();

};


#endif
