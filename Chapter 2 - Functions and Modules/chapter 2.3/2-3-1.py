def factorial(n):
    if n == 1: return 1
    return n * factorial(n-1)

#print(factorial(-5))
#RecursionError: maximum recursion depth exceeded in comparison
#it will run indefinitely as no base case will be reached
print(factorial(350))
#just prints hugh numbers
#123587405826548875014395199766546457224532073946919515879429330230093035357491314216934583295011178445941552109432761532449767761892237043444942213964090091669490545661255111334533069825455607852789836451585122902099649977304226794874840601811017764137584868137504975397325925882541777117706619490238363409254589994079334626893194608016888986949684994333459029365214555784862353939102567266745712846824819004146064184543888123533464975621179287075018586481357643313075153359002713294611632614208134036650116689052585573350955360246170451786972351365370405722036294385680478287278827977511411909071460914807681131728232182991517416470483157998067487290163200000000000000000000000000000000000000000000000000000000000000000000000000000000000000
