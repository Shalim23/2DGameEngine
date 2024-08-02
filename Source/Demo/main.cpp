//#define SDL_MAIN_HANDLED
//#include "SDL.h"
#include "Application.h"
#include <iostream>

int main()
{
#if EDITOR
    std::cout << "Editor\n";
#elif NDEBUG
    std::cout << "Release\n";

#else
    std::cout << "Debug\n";

#endif
    Application a;
    a.test();
    return 0;
}
