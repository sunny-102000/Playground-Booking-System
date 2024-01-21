#include <iostream>
#include <vector>
#include <algorithm>
#include <functional>

using namespace std;


//-------------------------------------------------------------//
//			Side-effect-free functions start				   //
//-------------------------------------------------------------//
int add(int a, int b)
{
	return a + b;
}
//-------------------------------------------------------------//
//			Side-effect-free functions	stop				   //
//-------------------------------------------------------------//





//////////////////////////////////////////////////////////////////////////////////////////////////////




//-------------------------------------------------------------//
//			use of higher-order functions start				   //
//-------------------------------------------------------------//
void applyOperation(const vector<int>& numeros, function<int(int)> operation)
{
	for (int numer : numeros)
	{
		cout << operation(numer) << " ";
	}
	cout << endl;
}
//-------------------------------------------------------------//
//			use of higher-order functions stop				   //
//-------------------------------------------------------------//




//////////////////////////////////////////////////////////////////////////////////////////////////////




//-------------------------------------------------------------//
//		functions as parameters and return values start		   //
//-------------------------------------------------------------//
int funaspar(int a, int b, function<int(int, int)> operation)
{
	return operation(a, b);
}

function<int(int)> createMultiplier(int factor)
{
	return [factor](int x) {return x * factor; };
}
//-------------------------------------------------------------//
//		functions as parameters and return values stop		   //
//-------------------------------------------------------------//



int main()
{

	
	//-------------------------------------------------------------//
	//				Only final data structures					   //
	//-------------------------------------------------------------//
	cout << "Only final data structures" << endl << endl;


	vector<int> numbers = { 1,2,3,4,5 };
	vector<int> sqareNumbers;

	transform(numbers.begin(), numbers.end(), back_inserter(sqareNumbers), [](int x) {return x * x; });

	cout << "Used numbers: ";

	for (int num : numbers)
	{
		cout << num << " ";
	}

	cout << "\nSquared numbers: ";

	for (int squared : sqareNumbers)
	{
		cout << squared << " ";
	}

	cout << endl << "---------------------------------------------------------------------------------------------" << endl;

	
	//-------------------------------------------------------------//
	//				 Side-effect-free functions					   //
	//-------------------------------------------------------------//
	cout << endl << endl << endl << "Side-effect-free functions" << endl << endl;


	int x = 5;
	int y = 10;

	int result = add(x, y);

	cout << "Adding " << x << " + " << y << " = " << result << endl;


	cout << "---------------------------------------------------------------------------------------------" << endl;
	
	//-------------------------------------------------------------//
	//			use of higher-order functions					   //
	//-------------------------------------------------------------//
	cout << endl << endl << "use of higher-order functions" << endl << endl;

	vector<int> numeros = { 1,2,3,4,5 };

	cout << "Used numbers: ";

	for (int nymer : numeros)
	{
		cout << nymer << " ";
	}

	cout << endl;

	cout << "Sqared numbers: ";
	applyOperation(numeros, [](int x) {return x * x; });

	cout << "Doubled numbers: ";
	applyOperation(numeros, [](int x) {return x * 2; });

	cout << "---------------------------------------------------------------------------------------------" << endl;
	
	//-------------------------------------------------------------//
	//		functions as parameters and return values			   //
	//-------------------------------------------------------------//
	cout << endl << endl << "functions as parameters and return values" << endl << endl;

	int result1 = funaspar(5, 3, [](int a, int b) {return a + b; });

	cout << "Result of adding: " << result1 << endl;

	auto multiplier = createMultiplier(3);
	int result2 = multiplier(4);
	cout << "result of multiplaying: " << result2 << std::endl;

	cout << "---------------------------------------------------------------------------------------------" << endl;
	
	//-------------------------------------------------------------//
	//		use closures / anonymous functions (using closures)	   //
	//-------------------------------------------------------------//
	cout << endl << endl << "use closures / anonymous functions (using closures)" << endl << endl;

	int opd = 3;
	auto multiplyByOpd = [opd](int x) {return x * opd; };

	int opdResult = multiplyByOpd(7);
	cout << "OPD result: " << opdResult << endl;

	cout << "---------------------------------------------------------------------------------------------" << endl;
}
