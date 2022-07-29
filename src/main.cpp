#include <iostream>
#include <vector>
#include <sstream>
#include <algorithm>


#include "Notas.hpp"
#include "NotasDB.hpp"
#include "Pessoa.hpp"


using namespace std;


// o objetivo desse programa é fazer um backend 
// agora só irei fazer assim por enquanto

int main(void){
	string nome;

	cout << "Qual o seu nome?" << endl;
	getline(cin, nome);

	// usar find
	vector <string> possiveis_nao = {"não", "NÃO", "nao", "n", "Não"};
	vector <string> possiveis_sim = {"sim", "SIM", "s", "Sim", "y"};
	vector < vector <string> > escolhas = {possiveis_nao, possiveis_sim};


	string escolha; int opcao = -1; // 0 para nao, 1 para sim e -1 para indefinido
	cout << "Quer notar alguma coisa? " << endl;
	cin >> escolha;

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
		break;
	}

	return 0;
}


