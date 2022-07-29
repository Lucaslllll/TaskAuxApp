#ifdef NotasDB_hpp
#define NotasDB_hpp

#include <iostream>
#include <vector>
#include <sstream>
#include <algorithm>

#include "Notas.hpp"


// classe para NotasDB servirá para salvar seja em txt ou em sql
class NotasDB{


private:


public:
	NotasDB();

	void salvar(Notas *nota);
	void deletar(Notas *nota);


};


#endif
