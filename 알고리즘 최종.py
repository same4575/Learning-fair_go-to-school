print("등교 게임에 오신 것을 환영합니다.")
print("여러분은 지금부터 상명대학교 어느 강의실에에서 발생하는 여러 미니게임들을 통과해야지만")
print("이 게임에서 탈출하실 수 있습니다")

while True :
    a = input('찾으시는 강의실을 말씀해주세요. ex) a101이면 a :' )

    if a == 'a':
        print('사범대학 입니다. 우리가 찾는 강의실은 이 곳이 아닙니다')

    elif a == 'b':
        print('미술가정관입니다. 우리가 찾는 강의실은 이 곳이 아닙니다')

    elif a == 'd':
        print('공예관 입니다. 우리가 찾는 강의실은 이 곳이 아닙니다')

    elif a == 'e':
        print('학군단 입니다. 우리가 찾는 강의실은 이 곳이 아닙니다')

    elif a == 'f':
        print('체육관 입니다. 우리가 찾는 강의실은 이 곳이 아닙니다')

    elif a == 'g':
        print('소프트웨어대학 입니다. 우리가 찾는 강의실은 이 곳이 아닙니다')

    elif a == 'h':
        print('학생회관 입니다. 우리가 찾는 강의실은 이 곳이 아닙니다')

    elif a == 'i':
        print('제 2 교수회관 입니다. 우리가 찾는 강의실은 이 곳이 아닙니다')

    elif a == 'j':
        print('대학본부  입니다. 우리가 찾는 강의실은 이 곳이 아닙니다')

    
    elif a == 'l':
        print('중앙도서관 입니다. 우리가 찾는 강의실은 이 곳이 아닙니다')
    
    elif a == 'm':
        print('종합관 입니다. 우리가 찾는 강의실은 이 곳이 아닙니다')

    elif a == 'n':
        print('자하관 입니다. 우리가 찾는 강의실은 이 곳이 아닙니다')

    elif a == 'o':
        print('제 1 교수회관 입니다. 우리가 찾는 강의실은 이 곳이 아닙니다')

    elif a == 'r':
        print('미래백년관 입니다. 우리가 찾는 강의실은 이 곳이 아닙니다')

    elif a == 's':
        print('인문사회과학 대학 입니다. 우리가 찾는 강의실은 이 곳이 아닙니다')

    elif a == 't':
        print('밀레니엄관 입니다. 우리가 찾는 강의실은 이 곳이 아닙니다')

    elif a == 'u':
        print('상명 아트센터 입니다. 우리가 찾는 강의실은 이 곳이 아닙니다')


    elif a == 'k':
        print('자연과학대학 입니다. 우리가 찾던 강의실 입니다!')
        from tkinter import *          #<- 미로찾기 게임 시작
        from tkinter import messagebox as msg
        import time
        import math
        import random


        window=Tk()
        window.title("미로 찾기")
        #window.geometry("850x490")

        WIDTH=700
        HEIGHT=490

        canvas=Canvas(window, width=WIDTH, height=HEIGHT, bg="black")
        canvas.pack(side="right")

            

        


        def p_move(event):
            global x,y,score
    
    
    
            if event.keysym=="Up" and maze[y-1][x]!=1:
                canvas.move(p, 0, -70)
                y-=1
            elif event.keysym=="Down"and maze[y+1][x]!=1:
                canvas.move(p,0,70)
                y+=1
            elif event.keysym=="Left"and maze[y][x-1]!=1:
                canvas.move(p,-70,0)
                x-=1
            elif event.keysym=="Right"and maze[y][x+1]!=1:
                canvas.move(p,70,0)
                x+=1

            if score>=3:
                if maze[y][x]==2:
                    msgbox=msg.askquestion("미션 성공", "미션 성공! 그럼 다음단계로 넘어가겠습니다.")
                    if msgbox=="yes":
                        window.destroy()


                        # 다음 게임 (수학게임)
                        import random

                        number_amount = 0
                        difficulty = 4

                        life = 3

                        sum = 0

                        num1 = 0
                        num2 = 0
                        num3 = 0
                        num4 = 0

                        equ1 = 0
                        equ2 = 0
                        equ3 = 0
                        equ4 = 0

                        formula1 = 0
                        formula2 = 0
                        formula3 = 0

                        answer1 = 0
                        answer2 = 0
                        answer3 = 0



                        while difficulty >= 4:
                            difficulty = int(input("원하는 난이도를 정해주세요. (1: 쉬움 / 2: 보통 / 3: 어려움 / 0: 종료)"))

                            if difficulty == 1:
                                number_amount = 2
                            elif difficulty == 2:
                                number_amount = 3
                            elif difficulty == 3:
                                number_amount = 4
                            elif difficulty == 0:
                                print("게임을 종료합니다 ^오^")
        

                        if difficulty != 0:

                            if difficulty == 1:
                                print("쉬움 난이도를 선택하셨습니다. (생성되는 숫자 수: 2개, 목숨: 3개)")
                                num1 = random.choice(range(1, 10))
                                num2 = random.choice(range(1, 10))
                                equ1 = random.choice(range(1, 4))
                                equ2 = random.choice(range(1, 4))
                            elif difficulty == 2:
                                print("보통 난이도를 선택하셨습니다. (생성되는 숫자 수: 3개, 목숨: 3개)")
                                num1 = random.choice(range(1, 10))
                                num2 = random.choice(range(1, 10))
                                num3 = random.choice(range(1, 10))
                                equ1 = random.choice(range(1, 4))
                                equ2 = random.choice(range(1, 4))
                                equ3 = random.choice(range(1, 4))
                            elif difficulty == 3:
                                print("어려움 난이도를 선택하셨습니다. (생성되는 숫자 수: 4개, 목숨: 3개)")
                                num1 = random.choice(range(1, 10))
                                num2 = random.choice(range(1, 10))
                                num3 = random.choice(range(1, 10))
                                num4 = random.choice(range(1, 10))
                                equ1 = random.choice(range(1, 4))
                                equ2 = random.choice(range(1, 4))
                                equ3 = random.choice(range(1, 4))
                                equ4 = random.choice(range(1, 4))
    


                            if equ1 == 1:
                                cal1 = num1*1
                                formula1 = formula1+1
                            elif equ1 == 2:
                                cal1 = num1*2
                                formula2 = formula2+1
                            elif equ1 == 3:
                                cal1 = num1**2
                                formula3 = formula3+1

                            if equ2 == 1:
                                cal2 = num2*1
                                formula1 = formula1+1
                            elif equ2 == 2:
                                cal2 = num2*2
                                formula2 = formula2+1
                            elif equ2 == 3:
                                cal2 = num2**2
                                formula3 = formula3+1

                            if equ3 == 1:
                                cal3 = num3*1
                                formula1 = formula1+1
                            elif equ3 == 2:
                                cal3 = num3*2
                                formula2 = formula2+1
                            elif equ3 == 3:
                                cal3 = num3**2
                                formula3 = formula3+1

                            if equ4 == 1:
                                cal4 = num4*1
                                formula1 = formula1+1
                            elif equ4 == 2:
                                cal4 = num4*2
                                formula2 = formula2+1
                            elif equ4 == 3:
                                cal4 = num4**2
                                formula3 = formula3+1


                            print("공식 1: *1, 공식 2: *2, 공식 3: **2")
    
    
    
                            if difficulty == 1:
                                sum = cal1+cal2
                                print("첫번째 숫자는 %d 입니다." % num1)
                                print("두번째 숫자는 %d 입니다." % num2)
        
        
                            elif difficulty == 2:
                                sum = cal1+cal2+cal3
                                print("첫번째 숫자는 %d 입니다." % num1)
                                print("두번째 숫자는 %d 입니다." % num2)
                                print("세번째 숫자는 %d 입니다." % num3)
        
                            elif difficulty == 3:
                                sum = cal1+cal2+cal3+cal4
                                print("첫번째 숫자는 %d 입니다." % num1)
                                print("두번째 숫자는 %d 입니다." % num2)
                                print("세번째 숫자는 %d 입니다." % num3)
                                print("네번째 숫자는 %d 입니다." % num4)
        
        

                            print("각 숫자를 공식에 대입한 후의 숫자의 총합은 %d 입니다." % sum)
                            print("사용된 공식은 다음과 같습니다.")
                            print("*1: %d 회" % formula1)
                            print("*2: %d 회" % formula2)
                            print("**2: %d 회" % formula3)

                            while life != 0:
                                if difficulty == 1:
                                    answer1 = int(input("첫번째 숫자에 사용된 공식을 적어주세요.(1: *1 // 2: *2 // 3: **2)"))
                                    answer2 = int(input("두번째 숫자에 사용된 공식을 적어주세요.(1: *1 // 2: *2 // 3: **2)"))
                                    if answer1 == equ1 and answer2 == equ2:
                                        print("정답입니다!")
                                        break
                                    else:
                                        life = life - 1
                                        print("틀렸습니다. 목숨이 1 감소합니다.")
                                elif difficulty == 2:
                                    answer1 = int(input("첫번째 숫자에 사용된 공식을 적어주세요.(1: *1 // 2: *2 // 3: **2)"))
                                    answer2 = int(input("두번째 숫자에 사용된 공식을 적어주세요.(1: *1 // 2: *2 // 3: **2)"))
                                    answer3 = int(input("세번째 숫자에 사용된 공식을 적어주세요.(1: *1 // 2: *2 // 3: **2)"))
                                    if answer1 == equ1 and answer2 == equ2 and answer3 == equ3:
                                        print("정답입니다!")
                                        break
                                    else:
                                        life = life - 1
                                        print("틀렸습니다. 목숨이 1 감소합니다.")
                                elif difficulty == 3:
                                    answer1 = int(input("첫번째 숫자에 사용된 공식을 적어주세요.(1: *1 // 2: *2 // 3: **2)"))
                                    answer2 = int(input("두번째 숫자에 사용된 공식을 적어주세요.(1: *1 // 2: *2 // 3: **2)"))
                                    answer3 = int(input("세번째 숫자에 사용된 공식을 적어주세요.(1: *1 // 2: *2 // 3: **2)"))
                                    answer4 = int(input("네번째 숫자에 사용된 공식을 적어주세요.(1: *1 // 2: *2 // 3: **2)"))
                                    if answer1 == equ1 and answer2 == equ2 and answer3 == equ3 and answer4 == equ4:
                                        print("정답입니다!")
                                        break
                                    else:
                                        life = life - 1
                                        print("틀렸습니다. 목숨이 1 감소합니다.")

                            if life == 0:
                                print("")
                                print("")
                                print("")
                                print("게임 오버...")
                                print("게임에서 탈락하셨습니다...!")
                            else:
                                print("")
                                print("")
                                print("게임 클리어! 그럼 마지막 단계, 홀짝 게임으로 넘어가겠습니다.")
                                import random
#import os
#import time
# 홀짝 게임 시작

                                life = 5
                                score = 0
                                print("")
                                print("지금부터 홀짝게임을 시작하겠습니다.")
                                print("숫자는 무작위로 선정되며 여러분은 그 숫자가 홀수인지, 짝수인지 맞추어 주시기를 바랍니다.")
                                print("홀수라고 생각하시면 0, 짝수라고 생각하시면 1을 입력해주세요")
                                print("생명은 5개 이고, 한 문제당 100점씩 300점을 채우시면 통과입니다")
                                while 1:
                                    if score == 300:
                                        print("")
                                        print("")
                                        print("")
                                        print(" 축하합니다. 게임에서 통과하셨습니다!!")
                                        print("")
                                        print(" 등교게임에 통과한 당신!  이제 상명대를 더 제대로 알고 더 사랑하는 마음으로 다니기를 바랍니다! ")
                                        break
                                    if life == 0:
                                        print("")
                                        print("")
                                        print("총 점수 : ", score)
                                        print("")
                                        print("게임 종료")
                                        print("게임에서 탈락하셨습니다...")
                                        break

                                    marblegame = random.randint(10,99)

                                    print("점수 : {}, 목숨 : {}".format(score, life))
                                    user = int(input("홀(0), 짝(1) : "))

                                    print("정답 : {}".format(marblegame), end='/ ')

                                    if user:
                                        if marblegame % 2:
                                            print("틀렸습니다.")
                                            life -= 1
                                        else:
                                            print("맞았습니다.")
                                            score += 100
                                    else:
                                        if marblegame % 2:
                                            print("맞았습니다.")
                                            score += 100
                                        else:
                                            print("틀렸습니다.")
                                            life -= 1

    #time.sleep(2)               # 프로그램을 잠시 멈춤
    #os.system("cls")            # 화면을 바꿔줌
    
                                

                        window.destroy() 
                    else:
                        # 다음 게임 (수학게임)
                        import random

                        number_amount = 0
                        difficulty = 4

                        life = 3

                        sum = 0

                        num1 = 0
                        num2 = 0
                        num3 = 0
                        num4 = 0

                        equ1 = 0
                        equ2 = 0
                        equ3 = 0
                        equ4 = 0

                        formula1 = 0
                        formula2 = 0
                        formula3 = 0

                        answer1 = 0
                        answer2 = 0
                        answer3 = 0



                        while difficulty >= 4:
                            difficulty = int(input("원하는 난이도를 정해주세요. (1: 쉬움 / 2: 보통 / 3: 어려움 / 0: 종료)"))

                            if difficulty == 1:
                                number_amount = 2
                            elif difficulty == 2:
                                number_amount = 3
                            elif difficulty == 3:
                                number_amount = 4
                            elif difficulty == 0:
                                print("게임을 종료합니다 ^오^")
        

                        if difficulty != 0:

                            if difficulty == 1:
                                print("쉬움 난이도를 선택하셨습니다. (생성되는 숫자 수: 2개, 목숨: 3개)")
                                num1 = random.choice(range(1, 10))
                                num2 = random.choice(range(1, 10))
                                equ1 = random.choice(range(1, 4))
                                equ2 = random.choice(range(1, 4))
                            elif difficulty == 2:
                                print("보통 난이도를 선택하셨습니다. (생성되는 숫자 수: 3개, 목숨: 3개)")
                                num1 = random.choice(range(1, 10))
                                num2 = random.choice(range(1, 10))
                                num3 = random.choice(range(1, 10))
                                equ1 = random.choice(range(1, 4))
                                equ2 = random.choice(range(1, 4))
                                equ3 = random.choice(range(1, 4))
                            elif difficulty == 3:
                                print("어려움 난이도를 선택하셨습니다. (생성되는 숫자 수: 4개, 목숨: 3개)")
                                num1 = random.choice(range(1, 10))
                                num2 = random.choice(range(1, 10))
                                num3 = random.choice(range(1, 10))
                                num4 = random.choice(range(1, 10))
                                equ1 = random.choice(range(1, 4))
                                equ2 = random.choice(range(1, 4))
                                equ3 = random.choice(range(1, 4))
                                equ4 = random.choice(range(1, 4))
    


                            if equ1 == 1:
                                cal1 = num1*1
                                formula1 = formula1+1
                            elif equ1 == 2:
                                cal1 = num1*2
                                formula2 = formula2+1
                            elif equ1 == 3:
                                cal1 = num1**2
                                formula3 = formula3+1

                            if equ2 == 1:
                                cal2 = num2*1
                                formula1 = formula1+1
                            elif equ2 == 2:
                                cal2 = num2*2
                                formula2 = formula2+1
                            elif equ2 == 3:
                                cal2 = num2**2
                                formula3 = formula3+1

                            if equ3 == 1:
                                cal3 = num3*1
                                formula1 = formula1+1
                            elif equ3 == 2:
                                cal3 = num3*2
                                formula2 = formula2+1
                            elif equ3 == 3:
                                cal3 = num3**2
                                formula3 = formula3+1

                            if equ4 == 1:
                                cal4 = num4*1
                                formula1 = formula1+1
                            elif equ4 == 2:
                                cal4 = num4*2
                                formula2 = formula2+1
                            elif equ4 == 3:
                                cal4 = num4**2
                                formula3 = formula3+1


                            print("공식 1: *1, 공식 2: *2, 공식 3: **2")
    
    
    
                            if difficulty == 1:
                                sum = cal1+cal2
                                print("첫번째 숫자는 %d 입니다." % num1)
                                print("두번째 숫자는 %d 입니다." % num2)
        
        
                            elif difficulty == 2:
                                sum = cal1+cal2+cal3
                                print("첫번째 숫자는 %d 입니다." % num1)
                                print("두번째 숫자는 %d 입니다." % num2)
                                print("세번째 숫자는 %d 입니다." % num3)
        
                            elif difficulty == 3:
                                sum = cal1+cal2+cal3+cal4
                                print("첫번째 숫자는 %d 입니다." % num1)
                                print("두번째 숫자는 %d 입니다." % num2)
                                print("세번째 숫자는 %d 입니다." % num3)
                                print("네번째 숫자는 %d 입니다." % num4)
        
        

                            print("각 숫자를 공식에 대입한 후의 숫자의 총합은 %d 입니다." % sum)
                            print("사용된 공식은 다음과 같습니다.")
                            print("*1: %d 회" % formula1)
                            print("*2: %d 회" % formula2)
                            print("**2: %d 회" % formula3)

                            while life != 0:
                                if difficulty == 1:
                                    answer1 = int(input("첫번째 숫자에 사용된 공식을 적어주세요.(1: *1 // 2: *2 // 3: **2)"))
                                    answer2 = int(input("두번째 숫자에 사용된 공식을 적어주세요.(1: *1 // 2: *2 // 3: **2)"))
                                    if answer1 == equ1 and answer2 == equ2:
                                        print("정답입니다!")
                                        break
                                    else:
                                        life = life - 1
                                        print("틀렸습니다. 목숨이 1 감소합니다.")
                                elif difficulty == 2:
                                    answer1 = int(input("첫번째 숫자에 사용된 공식을 적어주세요.(1: *1 // 2: *2 // 3: **2)"))
                                    answer2 = int(input("두번째 숫자에 사용된 공식을 적어주세요.(1: *1 // 2: *2 // 3: **2)"))
                                    answer3 = int(input("세번째 숫자에 사용된 공식을 적어주세요.(1: *1 // 2: *2 // 3: **2)"))
                                    if answer1 == equ1 and answer2 == equ2 and answer3 == equ3:
                                        print("정답입니다!")
                                        break
                                    else:
                                        life = life - 1
                                        print("틀렸습니다. 목숨이 1 감소합니다.")
                                elif difficulty == 3:
                                    answer1 = int(input("첫번째 숫자에 사용된 공식을 적어주세요.(1: *1 // 2: *2 // 3: **2)"))
                                    answer2 = int(input("두번째 숫자에 사용된 공식을 적어주세요.(1: *1 // 2: *2 // 3: **2)"))
                                    answer3 = int(input("세번째 숫자에 사용된 공식을 적어주세요.(1: *1 // 2: *2 // 3: **2)"))
                                    answer4 = int(input("네번째 숫자에 사용된 공식을 적어주세요.(1: *1 // 2: *2 // 3: **2)"))
                                    if answer1 == equ1 and answer2 == equ2 and answer3 == equ3 and answer4 == equ4:
                                        print("정답입니다!")
                                        break
                                    else:
                                        life = life - 1
                                        print("틀렸습니다. 목숨이 1 감소합니다.")

                            if life == 0:
                                print("")
                                print("")
                                print("")
                                print("게임 오버...")
                                print("게임에서 탈락하셨습니다...!")
                            else:
                                print("")
                                print("")
                                print("게임 클리어! 그럼 마지막 단계, 홀짝 게임으로 넘어가겠습니다.")
                                import random
#import os
#import time
# 홀짝 게임 시작

                                life = 5
                                score = 0
                                print("")
                                print("지금부터 홀짝게임을 시작하겠습니다.")
                                print("숫자는 무작위로 선정되며 여러분은 그 숫자가 홀수인지, 짝수인지 맞추어 주시기를 바랍니다.")
                                print("홀수라고 생각하시면 0, 짝수라고 생각하시면 1을 입력해주세요")
                                print("생명은 5개 이고, 한 문제당 100점씩 300점을 채우시면 통과입니다")
                                while 1:
                                    if score == 300:
                                        print("")
                                        print("")
                                        print("")
                                        print(" 축하합니다. 게임에서 통과하셨습니다!!")
                                        print("")
                                        print(" 등교게임에 통과한 당신!  이제 상명대를 더 제대로 알고 더 사랑하는 마음으로 다니기를 바랍니다! ")
                                        break
                                    if life == 0:
                                        print("")
                                        print("")
                                        print("총 점수 : ", score)
                                        print("")
                                        print("게임 종료")
                                        print("게임에서 탈락하셨습니다...")
                                        break

                                    marblegame = random.randint(10,99)

                                    print("점수 : {}, 목숨 : {}".format(score, life))
                                    user = int(input("홀(0), 짝(1) : "))

                                    print("정답 : {}".format(marblegame), end='/ ')

                                    if user:
                                        if marblegame % 2:
                                            print("틀렸습니다.")
                                            life -= 1
                                        else:
                                            print("맞았습니다.")
                                            score += 100
                                    else:
                                        if marblegame % 2:
                                            print("맞았습니다.")
                                            score += 100
                                        else:
                                            print("틀렸습니다.")
                                            life -= 1


                        window.destroy()

            if p_coor[0]==290 and p_coor[1]==10:
                score+=1
                canvas.move(st1, 0, -1000)
    
            if p_coor[0]==430 and p_coor[1]==80:
                score+=1
                canvas.move(st2, 0, -1000)

            if p_coor[0]==640 and p_coor[1]==430:
                score+=1
                canvas.move(st3, 0, 1000)
    
 

        def enemy_move():
            global x_speed,p_coor
            enemy_coor=canvas.coords(enemy)
            canvas.move(enemy, x_speed, 0)

            if enemy_coor[2]>=700:
                x_speed = -5
            elif enemy_coor[0]<=70:
                x_speed = 5

            p_coor=canvas.coords(p)
    
            if enemy_coor[0]==p_coor[2] and enemy_coor[1]==p_coor[1] or enemy_coor[2]==p_coor[0] and enemy_coor[1]==p_coor[1]:
                msgbox=msg.askquestion("미션 실패", "미션 실패!")
                if msgbox=="yes":
                   print("")
                   print("")
                   print("") 
                   print("게임에서 탈락하셨습니다...!")
                   window.destroy()
                else:
                    print("")
                    print("")
                    print("") 
                    print("게임에서 탈락하셨습니다...!")
                    window.destroy()




    





        maze=[
            [0,0,1,1,3,1,1,1,1,1],
            [1,0,0,1,0,1,3,0,0,1],
            [1,1,0,1,0,0,1,1,0,1],
            [1,0,0,1,1,0,0,1,0,1],
            [1,0,1,1,0,1,0,1,0,1],
            [1,0,0,0,0,0,0,0,0,0],
            [2,0,1,1,1,1,1,1,1,3]
        ]




        for y in range(7):
            for x in range(10):
                if maze[y][x]==1:
                    canvas.create_rectangle(x*70, y*70, (x+1)*70, (y+1)*70,
                                            fill="grey", outline="white")
        


        x=0
        y=0
    
        score=0


        st1=canvas.create_oval(290,10,340,60,
                               fill="yellow", outline="yellow")

        st2=canvas.create_oval(430,80,480,130,
                               fill="yellow", outline="yellow")
        st3=canvas.create_oval(640,430,690,480,
                               fill="yellow", outline="yellow")


        p=canvas.create_oval(10, 10, 60, 60,
                             fill="white", outline="black", width=2)
        canvas.bind_all("<KeyPress>", p_move)
        
        pt=canvas.create_rectangle(10, 430, 62, 480,
                                   fill="blue", outline="white")
    


        enemy=canvas.create_oval(80,360,130,410,
                                  fill="red")
    

        x_speed=5


        while True:
            enemy_move()
            window.update()
            time.sleep(0.009)
    


        window.mainloop()

        
    

    
