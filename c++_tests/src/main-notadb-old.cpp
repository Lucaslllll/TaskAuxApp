#include <iostream>
#include <vector>
#include <sstream>
#include <algorithm>

#include "NotasDB.hpp"
#include "Pessoa.hpp"
#include "Notas.hpp"



using namespace std;


// o objetivo desse programa é fazer um backend 
// agora só irei fazer assim por enquanto

int main(void){
	string nome, data, nome_nota;
    NotasDB *notadb = new NotasDB();
    
    

	cout << "Qual o seu nome?" << endl;
	getline(cin, nome);

	// usar find
	vector <string> possiveis_nao = {"não", "NÃO", "nao", "n", "Não"};
	vector <string> possiveis_sim = {"sim", "SIM", "s", "Sim", "y"};
	vector < vector <string> > escolhas = {possiveis_nao, possiveis_sim};


	string escolha; int opcao = -1; // 0 para nao, 1 para sim e -1 para indefinido
	cout << "Quer notar alguma coisa? " << endl;
	getline(cin, escolha);

	for(int i = 0; i < 2; i++){
		for(int j = 0; j < escolhas[i].size(); j++){
			if(escolhas[i][j].find(escolha) != string::npos){
				opcao = i;
			}
		}
	}

	switch(opcao){
		case -1:
			cout << "Resposta Desconhecida" << endl;
		break;
		case 0:
			cout << "Encerrando Programa" << endl;
			exit(EXIT_SUCCESS);
		break;
		case 1:
			cout << "Abrindo Notas..." << endl;
            
            cout << "Mas Antes Digite O Nome Da Nota: " << endl;
            getline(cin, nome_nota);
            cout << "Digite A Data Da Nota No Formato (dd-mm-aaaa) : " << endl;
            getline(cin, data);
            Pessoa *pessoa = new Pessoa(nome);
            
            
            
            Notas *nota = new Notas(nome_nota, data, pessoa);
            
            cout << "Escreva A Baixo Seu Texto E Para Sair Digite //q " << endl;
            while(true){
                string linha;
                getline(cin, linha);
                // para adicionar quebra de linha, ja que getline nao salvar quebra
                linha = linha + "\n"; 
                if(linha.find("//q") != string::npos){
                    break;
                }
                nota->add_detalhes(linha);
            }
            // no backend criar sistema de login para nao pedir os dados do usuario
            // adicionar sistema de som de alarme
            
            
            
            cout << "Deseja Salvar Sua Nota Na DataBase? y/n ";
            getline(cin, escolha);
            if(escolha == "y")
                notadb->salvar(nota);
            
            
            delete pessoa;
            
		break;

	}

	delete notadb;
	return 0;
}


