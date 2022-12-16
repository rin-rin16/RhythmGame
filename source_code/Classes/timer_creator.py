import numpy as np
from source_code.Sound_Rhytm.songs_bpm import songs_bpm as sb

arr_K_K = np.arange(0, 78, 60 / 1370)
l_K_K = []

for i in arr_K_K:
    if i >= 8.4:
        if (
                ((((i + sb.K_K[1]) / (60 / sb.K_K[0])) % 8 <= 60 / 1370) or
                (((i + sb.K_K[1]) / (60 / sb.K_K[0])) % 8 >= 8 - 60 / 1370)) or

                ((((i + sb.K_K[1]) / (60 / sb.K_K[0])) % 8 <= 2 + 60 / 1370) and
                 (((i + sb.K_K[1]) / (60 / sb.K_K[0])) % 8 >= 2 - 60 / 1370)) or

                ((((i + sb.K_K[1]) / (60 / sb.K_K[0])) % 8 <= 4 + 60 / 1370) and
                 (((i + sb.K_K[1]) / (60 / sb.K_K[0])) % 8 >= 4 - 60 / 1370)) or

                ((((i + sb.K_K[1]) / (60 / sb.K_K[0])) % 8 <= 6 + 60 / 1370) and
                 (((i + sb.K_K[1]) / (60 / sb.K_K[0])) % 8 >= 6 - 60 / 1370)) or

                ((((i + sb.K_K[1]) / (60 / sb.K_K[0])) % 8 <= 1 + 60 / 1370) and
                 (((i + sb.K_K[1]) / (60 / sb.K_K[0])) % 8 >= 1 - 60 / 1370))
            ):
            l_K_K.append(i)


arr_L_A_D = np.arange(0, 134, 60 / 1150)
l_L_A_D = []
for i in arr_L_A_D:
    if i >= 1.5 and i<= 132:
        if(    not
                    ((((i + sb.L_A_D[1]) <= 16.5) and
                    ((i + sb.L_A_D[1]) >= 14.5)) or

                     (((i + sb.L_A_D[1]) <= 49.6) and
                      ((i + sb.L_A_D[1]) >= 47.7)) or

                     (((i + sb.L_A_D[1]) <= 66.5) and
                      ((i + sb.L_A_D[1]) >= 64.5)) or

                      (((i + sb.L_A_D[1]) <= 99.75) and
                       ((i + sb.L_A_D[1]) >= 97.75)) or

                     (((i + sb.L_A_D[1]) <= 116.5) and
                      ((i + sb.L_A_D[1]) >= 114.5))
                    )

                    and
                    (((i + sb.L_A_D[1]) % (60 / sb.L_A_D[0]) <= 60 / 1150/2) or
                    ((i + sb.L_A_D[1]) % (60 / sb.L_A_D[0]) >= 60 / sb.L_A_D[0] - 60 / 1150/2)

                    or

                    ((((i + sb.L_A_D[1]) <= 97)
                    and
                    ((i + sb.L_A_D[1]) >= 22))

                    and
                    ((((i + sb.L_A_D[1]) <= 25))
                    or
                     ((((i + sb.L_A_D[1]) >= 32)) and
                      ((i + sb.L_A_D[1]) <= 46))
                    or
                     ((((i + sb.L_A_D[1]) >= 72)) and
                      ((i + sb.L_A_D[1]) <= 76))
                    or
                     ((((i + sb.L_A_D[1]) >= 80)) and
                      ((i + sb.L_A_D[1]) <= 98))
                     )

                    and
                    (((((i + sb.L_A_D[1]) / (60 / sb.L_A_D[0])) % 8 <= 7.5 + 60 / 1150/2)) and
                    ((((i + sb.L_A_D[1]) / (60 / sb.L_A_D[0])) % 8 >= 7.5 - 60 / 1150/2)))))
                ):
            l_L_A_D.append(i)


arr_P_T = np.arange(0, 142, 60 / 1250)      # 143.5
l_P_T = []
for i in arr_P_T:
    if i > 0.4:
        if (not (((i + sb.P_T[1]) <= 15.7 and
                  (i + sb.P_T[1]) >= 13.5)
                 or
                 ((i + sb.P_T[1]) <= 46.5 and
                  (i + sb.P_T[1]) >= 44.25)
                 or
                 ((i + sb.P_T[1]) <= 92.5 and
                  (i + sb.P_T[1]) >= 91.25)
        )
                and
                (i + sb.P_T[1]) <= 136.5

                and

                (((((i + sb.P_T[1]) % (60 / sb.P_T[0]) <= 60 / 1250/2) or
                   ((i + sb.P_T[1]) % (60 / sb.P_T[0]) >= 60 / sb.P_T[0] - 60 / 1250/2)))

                 or

                 ((((((i + sb.P_T[1]) / (60 / sb.P_T[0])) % 16 <= 0.5 + 60 / 1250/2)) and
                   ((((i + sb.P_T[1]) / (60 / sb.P_T[0])) % 16 >= 0.5 - 60 / 1250/2))))
                 and not False

                )
        ):
            l_P_T.append(i)
        elif (
                ((i + sb.P_T[1]) <= 46.5 and
                 (i + sb.P_T[1]) >= 44.25)

                and
                ((((((i + sb.P_T[1]) / (60 / sb.P_T[0])) % 16 <= 14 + 60 / 1250/2)) and
                  ((((i + sb.P_T[1]) / (60 / sb.P_T[0])) % 16 >= 14 - 60 / 1250/2)))
                 or
                 (((((i + sb.P_T[1]) / (60 / sb.P_T[0])) % 16 <= 0 + 60 / 1250/2)) or
                  ((((i + sb.P_T[1]) / (60 / sb.P_T[0])) % 16 >= 16 - 60 / 1250/2)))
                )
        ):
            l_P_T.append(i)


arr_W_N = np.linspace(0, 164.9, 164900)     # Done
l_W_N = []
for i in arr_W_N:
    if (
            (i + sb.Y_N[1]) >= 37
            and
            (((i + sb.Y_N[1]) % (60 / sb.Y_N[0]) <= 0.0005) or
             ((i + sb.Y_N[1]) % (60 / sb.Y_N[0]) >= 60 / sb.Y_N[0] - 0.0005))
    ):
        l_W_N.append(i)
    elif (((i + sb.Y_N[1]) / (60 / sb.Y_N[0]) - 2) // 8 % 2 == 0

          and
          (i + sb.Y_N[1]) >= 4.75
          and
          ((i + sb.Y_N[1]) <= 36.2
           and
           (((i + sb.Y_N[1]) / (60 / sb.Y_N[0]) % 8 <= 3.5 + 0.0005) and
            ((i + sb.Y_N[1]) / (60 / sb.Y_N[0]) % 8 >= 3.5 - 0.0005)
            or
            ((i + sb.Y_N[1]) / (60 / sb.Y_N[0]) % 8 <= 2 + 0.0005) and
            ((i + sb.Y_N[1]) / (60 / sb.Y_N[0]) % 8 >= 2 - 0.0005)
            or
            ((i + sb.Y_N[1]) / (60 / sb.Y_N[0]) % 8 <= 5 + 0.0005) and
            ((i + sb.Y_N[1]) / (60 / sb.Y_N[0]) % 8 >= 5 - 0.0005)
            or
            ((i + sb.Y_N[1]) / (60 / sb.Y_N[0]) % 8 <= 7 + 0.0005) and
            ((i + sb.Y_N[1]) / (60 / sb.Y_N[0]) % 8 >= 7 - 0.0005)
            or
            ((i + sb.Y_N[1]) / (60 / sb.Y_N[0]) % 8 <= 1 + 0.0005) and
            ((i + sb.Y_N[1]) / (60 / sb.Y_N[0]) % 8 >= 1 - 0.0005)
            or
            ((i + sb.Y_N[1]) / (60 / sb.Y_N[0]) % 8 <= 0 + 0.0005) or
            ((i + sb.Y_N[1]) / (60 / sb.Y_N[0]) % 8 >= 8 - 0.0005)
            or
            ((i + sb.Y_N[1]) / (60 / sb.Y_N[0]) % 8 <= 0.5 + 0.0005) and
            ((i + sb.Y_N[1]) / (60 / sb.Y_N[0]) % 8 >= 0.5 - 0.0005)))
    ):
        l_W_N.append(i)
    elif (((i + sb.Y_N[1]) / (60 / sb.Y_N[0]) - 2) // 8 % 2 == 1

          and
          (i + sb.Y_N[1]) >= 4.75
          and
          ((i + sb.Y_N[1]) <= 36.2
           and
           (((i + sb.Y_N[1]) / (60 / sb.Y_N[0]) % 8 <= 3.5 + 0.0005) and
            ((i + sb.Y_N[1]) / (60 / sb.Y_N[0]) % 8 >= 3.5 - 0.0005)
            or
            ((i + sb.Y_N[1]) / (60 / sb.Y_N[0]) % 8 <= 2 + 0.0005) and
            ((i + sb.Y_N[1]) / (60 / sb.Y_N[0]) % 8 >= 2 - 0.0005)
            or
            ((i + sb.Y_N[1]) / (60 / sb.Y_N[0]) % 8 <= 5 + 0.0005) and
            ((i + sb.Y_N[1]) / (60 / sb.Y_N[0]) % 8 >= 5 - 0.0005)
            or
            ((i + sb.Y_N[1]) / (60 / sb.Y_N[0]) % 8 <= 7 + 0.0005) and
            ((i + sb.Y_N[1]) / (60 / sb.Y_N[0]) % 8 >= 7 - 0.0005)
            or
            ((i + sb.Y_N[1]) / (60 / sb.Y_N[0]) % 8 <= 0.75 + 0.0005) and
            ((i + sb.Y_N[1]) / (60 / sb.Y_N[0]) % 8 >= 0.75 - 0.0005)
            or
            ((i + sb.Y_N[1]) / (60 / sb.Y_N[0]) % 8 <= 1.25 + 0.0005) and
            ((i + sb.Y_N[1]) / (60 / sb.Y_N[0]) % 8 >= 1.25 - 0.0005)))

    ):
        l_W_N.append(i)
    elif 1.001 > i and i > 1:
        l_W_N.append(i)


arr_D_A = np.linspace(1, 31.4, 30400)
l_D_A = []
for i in arr_D_A:
    if (((i + sb.D_A[1]) % (60 / sb.D_A[0]) <= 0.0005) or
            ((i + sb.D_A[1]) % (60 / sb.D_A[0]) >= 60 / sb.D_A[0] - 0.0005)):
        l_D_A.append(i)