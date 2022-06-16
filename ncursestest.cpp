#include <ncurses.h>
#include <unistd.h>
#include <iostream>
#include <cstdlib>
#include <sstream>
#include <string>
//17 05 22
//this was made in an awkward way to try and get it to run on an Atari st with MiNT
//this version should run on a normal computer

std::string displaynum = "0000000" , answer = "" , selectchar;
int finalnum , ch , y = 0 , x = 0 , c98fix , storednum , tempnum;
bool run = true , add , minuss , multiply , divide , equals , refreshcalc = true;
int main(int argc, char *argv[]) {
 //setenv("TERM", "atari", true);

 initscr();
 noecho();
 curs_set(1);
 keypad(stdscr, TRUE);

while (run == true) {
    while (equals != true) {
        mvprintw(0, 0, displaynum.c_str());
        mvprintw(1, 0, "7|8|9 /");
        mvprintw(2, 0, "4|5|6 *");
        mvprintw(3, 0, "1|2|3 -");
        mvprintw(4, 0, " |0|  +");
        mvprintw(5, 0, "  =   E");
        mvprintw(6, 0, answer.c_str());
        mvprintw(7, 0, "Remember 16 bit");
        move(y, x);
            ch = getch();
            switch (ch){
                case KEY_UP:
                    y = (y - 1);
                    move(y, x);
                    refresh();
                    break;
                case KEY_DOWN:
                    y = (y + 1);
                    move(y, x);
                    refresh();
                    break;
                case KEY_RIGHT:
                    x = (x + 1);
                    move(y, x);
                    refresh();
                    break;
                case KEY_LEFT:
                    x = (x - 1);
                    move(y, x);
                    refresh();
                    break;
                case 10:
                    selectchar = inch();
                    if (selectchar == "+") {
                        if (displaynum == "0000000") {
                            mvprintw(9, 0,"you cant do that !!!!");
                            refresh();
                            sleep(1);
                        }
                        else {
                            storednum = finalnum;
                            displaynum = "0000000";
                            add = true;
                            refreshcalc = true;
                            refresh();
                        }
                        
                    }
                    else if (selectchar == "-") {
                        if (displaynum == "0000000") {
                            mvprintw(9, 0,"you cant do that !!!!");
                            refresh();
                            sleep(1);
                        }
                        else {
                            storednum = finalnum;
                            displaynum = "0000000";
                            minuss = true;
                            refresh();
                        }
                    }
                    else if (selectchar == "*") {
                        if (displaynum == "0000000") {
                            mvprintw(9, 0,"you cant do that !!!!");
                            refresh();
                            sleep(1);
                        }
                        else {
                            storednum = finalnum;
                            displaynum = "0000000";
                            multiply = true;
                            refresh();
                        }
                    }
                    else if (selectchar == "/") {
                        if (displaynum == "0000000") {
                            mvprintw(9, 0,"you cant do that !!!!");
                            refresh();
                            sleep(1);
                        }
                        else {
                            storednum = finalnum;
                            displaynum = "0000000";
                            divide = true;
                            refresh();
                        }
                    }
                    else if (selectchar == "=") {
                        if (displaynum == "0000000") {
                            mvprintw(9, 0,"you cant do that !!!!");
                            sleep(1);
                            refresh();
                        }
                        else {
                            //storednum = finalnum;
                            displaynum = "0000000";
                            equals = true;
                            refresh();
                        }
                    }
                    else if (selectchar == "E") {
                        run = false;
                        equals = true;
                    }
                    //im sorry for the terrible code next but c++ 98 caused problems so we have this now
                    else if (selectchar == "0"){
                        if (displaynum == "0000000"){
                            displaynum = "0";
                            finalnum = 0;
                        }
                        else{
                            finalnum = (finalnum * 10);
                            finalnum = (finalnum + 0);
                            std::ostringstream convert;
                            convert << finalnum;
                            displaynum = convert.str();
                            //displaynum = std::to_string(finalnum);
                        }
                    }
                    else if (selectchar == "1"){
                        if (displaynum == "0000000"){
                            displaynum = "1";
                            finalnum = 1;
                        }
                        else{
                            //more c++ 98 rubish I will clean this up later and turn into function
                            finalnum = (finalnum * 10);
                            finalnum = (finalnum + 1);
                            std::ostringstream convert;
                            convert << finalnum;
                            displaynum = convert.str();
                            //displaynum = std::to_string(finalnum);
                        }
                    }
                    else if (selectchar == "3"){
                        if (displaynum == "0000000"){
                            displaynum = "3";
                            finalnum = 3;
                        }
                        else{
                            finalnum = (finalnum * 10);
                            finalnum = (finalnum + 3);
                            std::ostringstream convert;
                            convert << finalnum;
                            displaynum = convert.str();
                            //displaynum = std::to_string(finalnum);
                        }
                    }
                    else if (selectchar == "4"){
                        if (displaynum == "0000000"){
                            displaynum = "4";
                            finalnum = 4;
                        }
                        else{
                            finalnum = (finalnum * 10);
                            finalnum = (finalnum + 4);
                            std::ostringstream convert;
                            convert << finalnum;
                            displaynum = convert.str();
                            //displaynum = std::to_string(finalnum);
                        }
                    }
                    else if (selectchar == "5"){
                        if (displaynum == "0000000"){
                            displaynum = "5";
                            finalnum = 5;
                        }
                        else{
                            finalnum = (finalnum * 10);
                            finalnum = (finalnum + 5);
                            std::ostringstream convert;
                            convert << finalnum;
                            displaynum = convert.str();
                            //displaynum = std::to_string(finalnum);
                        }
                    }
                    else if (selectchar == "6"){
                        if (displaynum == "0000000"){
                            displaynum = "6";
                            finalnum = 6;
                        }
                        else{
                            finalnum = (finalnum * 10);
                            finalnum = (finalnum + 6);
                            std::ostringstream convert;
                            convert << finalnum;
                            displaynum = convert.str();
                            //displaynum = std::to_string(finalnum);
                        }
                    }
                    else if (selectchar == "7"){
                        if (displaynum == "0000000"){
                            displaynum = "7";
                            finalnum = 7;
                        }
                        else{
                            finalnum = (finalnum * 10);
                            finalnum = (finalnum + 7);
                            std::ostringstream convert;
                            convert << finalnum;
                            displaynum = convert.str();
                            //displaynum = std::to_string(finalnum);
                        }
                    }
                    else if (selectchar == "8"){
                        if (displaynum == "0000000"){
                            displaynum = "8";
                            finalnum = 8;
                        }
                        else{
                            finalnum = (finalnum * 10);
                            finalnum = (finalnum + 8);
                            std::ostringstream convert;
                            convert << finalnum;
                            displaynum = convert.str();
                            //displaynum = std::to_string(finalnum);
                        }
                    }
                    else if (selectchar == "9"){
                        if (displaynum == "0000000"){
                            displaynum = "9";
                            finalnum = 9;
                        }
                        else{
                            finalnum = (finalnum * 10);
                            finalnum = (finalnum + 9);
                            std::ostringstream convert;
                            convert << finalnum;
                            displaynum = convert.str();
                            //displaynum = std::to_string(finalnum);
                        }
                    }
                    //does this annoy you it had better
                    else if (selectchar == "2"){
                        if (displaynum == "0000000"){
                            displaynum = "2";
                            finalnum = 2;
                        }
                        else{
                            finalnum = (finalnum * 10);
                            finalnum = (finalnum + 2);
                            std::ostringstream convert;
                            convert << finalnum;
                            displaynum = convert.str();
                            //displaynum = std::to_string(finalnum);
                        }
                    }
                
            }
    }
    if (add == true) {
        tempnum = (finalnum + storednum);
        std::ostringstream convert;
        convert << tempnum;
        answer = convert.str();
        //answer = std::to_string(tempnum);
        add = false;
        refresh();
    }
    else if (minuss == true){
        tempnum = (storednum - finalnum);
        std::ostringstream convert;
        convert << tempnum;
        answer = convert.str();
        //answer = std::to_string(tempnum);
        minuss == false;
        refresh();
    }
    else if (multiply == true) {
        tempnum = (finalnum * storednum);
        std::ostringstream convert;
        convert << tempnum;
        answer = convert.str();
        //answer = std::to_string(tempnum);
        multiply = false;
        refresh();
    }
    else if (divide == true) {
        try {
            tempnum = (storednum / finalnum);
            std::ostringstream convert;
            convert << tempnum;
            answer = convert.str();
            //answer = std::to_string(tempnum);
            divide = false;
            refresh();
        }
        catch(std::string answer) {
            answer = "you cannot divide by that";
            refresh();
        }
    }
    else {
        answer = "what something has failed";
        refresh();
    }
    equals = false;
    tempnum = 0;
    }
refresh();

//    refresh();
 sleep(1);

 endwin();
}
