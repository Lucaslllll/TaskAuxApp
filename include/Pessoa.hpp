#ifndef Pessoa_hpp
#define Pessoa_hpp

#include <iostream>

class Pessoa{
    private:
	unsigned int m_id;
        std::string m_nome; //<! nome da pessoa
        std::string m_data_nascimento; //<! data_nascimento



    public:
        /**
         * Construtor da classe pessoa.
         * Constroi um objeto do tipo pessoa com endereço inicializado com uma string vazia
         * @param nome o nome da pessoa
         * @param cpf o cpf da pessoa.
         */
        Pessoa(std::string nome);
	std::string getNome();

};

#endif //Pessoa_hpp
