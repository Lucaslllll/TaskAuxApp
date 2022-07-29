#ifndef Pessoa_hpp
#define Pessoa_hpp

#include <iostream>

class Pessoa{
    private:
        unsigned int m_id;
        std::string m_nome; //<! nome da pessoa
        std::string m_data_nascimento; //<! data_nascimento



    public:
        
        Pessoa(std::string nome);
        std::string get_nome();
        void set_data_nascimento(std::string nascimento);
        
        
};

#endif //Pessoa_hpp
