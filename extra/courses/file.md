## Подробный план четвертого модуля курса алгебры

### 6   Векторные пространства с ¯-билинейной формой

##### 6.1  ¯-Билинейные формы

-   Пр.-во билинейных форм: \$ \\mathrm{Bi}(V) \$ . Примеры билин. форм: \$ (v,w)\\mapsto v\^{\\scriptscriptstyle\\mathsf T}\\!\\cdot s\\cdot w \$ ( \$ V=K\^n \$ , \$ s\\in\\mathrm{Mat}(n,K) \$ ), \$ (f,g)\\mapsto\\!\\int\_\\alpha\^\\beta\\!\\!sfg \$ ( \$ V=\\mathrm C\^0\\!(\[\\alpha;\\beta\],\\mathbb R) \$ , \$ s\\in V \$ ).

-   Поля с инволюцией. Пространство \$ \\overline V \$ : \$ c\\overline\\cdot v=\\overline c\\,v \$ . Пространство ¯-билинейн. форм (полуторалинейных форм, если \$ \\overline{\\phantom c}\\ne\\mathrm{id}\_K \$ ): \$ \\overline\\mathrm{Bi}(V)=\\mathrm{Bi}(V,\\overline V,K) \$ .

-   Матрица Грама формы \$ \\sigma \$ : \$ {(\\sigma\_{e,e})}\_{j_1,j_2}\\!=\\sigma(e\_{j_1}\\!,e\_{j_2}) \$ . Обобщенная матрица Грама: \$ (\\sigma\_{(v_1,\\ldots,v_m),(w_1,\\ldots,w_m)})\_{j_1,j_2}\\!=\\sigma(v\_{j_1}\\!,w\_{j_2}) \$ . Теорема о матрице Грама.

    <span class="underline">Теорема о матрице Грама.</span> *Пусть \$ K \$ --- поле с инволюцией, \$ V \$ --- векторное простр.-во над \$ K \$ , \$ n=\\dim V\<\\infty \$ , \$ \\sigma\\in\\overline\\mathrm{Bi}(V) \$ и \$ e\\in\\mathrm{OB}(V) \$ ; тогда
    (1) для любых \$ v,w\\in V \$ выполнено \$ \\sigma(v,w)=(v\^e)\^{\\scriptscriptstyle\\mathsf T}\\!\\cdot\\sigma\_{e,e}\\!\\cdot\\overline{w\^e}=\\sum\_{j_1=1}\^n\\sum\_{j_2=1}\^n\\sigma\_{j_1,j_2}v\^{j_1}\\overline{w\^{j_2}} \$ (координаты вычисляются относительно \$ e \$ );
    (2) для любых \$ m\\in\\mathbb N_0 \$ и \$ v_1,\\ldots,v_m,w_1,\\ldots,w_m\\in V \$ выполнено \$ \\sigma\_{(v_1,\\ldots,v_m),(w_1,\\ldots,w_m)}\\!=\\bigl(v_1\^e\\;\\ldots\\;v_m\^e\\bigr)\^{\\scriptscriptstyle\\mathsf T}\\!\\cdot\\sigma\_{e,e}\\!\\cdot\\overline{\\bigl(w_1\^e\\;\\ldots\\;w_m\^e\\bigr)} \$ .*

-   Изоморфизм вект. пр.-в \$ \\biggl(\\!\\begin{align}\\overline\\mathrm{Bi}(V)&\\to\\mathrm{Mat}(n,K)\\\\\\sigma&\\mapsto\\sigma\_{e,e}\\end{align}\\!\\biggr) \$ . Преобразования при замене базиса: \$ \\sigma\_{\\tilde e,\\tilde e}=(\\mathrm c\_\\tilde e\^e)\^{\\scriptscriptstyle\\mathsf T}\\!\\cdot\\sigma\_{e,e}\\!\\cdot\\overline{\\mathrm c\_\\tilde e\^e} \$ и \$ \\sigma\_{\\tilde{j_1},\\tilde{j_2}}\\!=\\sum\_{l_1=1}\^n\\sum\_{l_2=1}\^n(e\_\\tilde{j_1})\^{l_1}\\overline{(e\_\\tilde{j_2})\^{l_2}}\\,\\sigma\_{l_1,l_2} \$ .

-   Простр.-ва ¯-симметричных форм и матриц: \$ \\overline\\mathrm{SBi}(V)=\\{\\sigma\\in\\overline\\mathrm{Bi}(V)\\mid\\forall\\,v,w\\in V\\;\\bigl(\\sigma(w,v)=\\overline{\\sigma(v,w)}\\bigr)\\} \$ и \$ \\overline\\mathrm S\\mathrm{Mat}(n,K)=\\{s\\in\\mathrm{Mat}(n,K)\\mid s\^{\\scriptscriptstyle\\mathsf T}\\!=\\overline s\\} \$ .

-   Пр.-ва ¯-антисимметр. форм и матриц: \$ \\overline\\mathrm{ABi}(V)=\\{\\sigma\\in\\overline\\mathrm{Bi}(V)\\mid\\forall\\,v,w\\in V\\;\\bigl(\\sigma(w,v)=-\\overline{\\sigma(v,w)}\\bigr)\\} \$ и \$ \\overline\\mathrm A\\mathrm{Mat}(n,K)=\\{s\\in\\mathrm{Mat}(n,K)\\mid s\^{\\scriptscriptstyle\\mathsf T}\\!=-\\overline s\\} \$ .

-   Гомоморфизмы между простр.-вами с ¯-билинейной формой: \$ \\mathrm{Hom}((V,\\sigma),(Y,\\varphi))=\\{a\\in\\mathrm{Hom}(V,Y)\\mid\\forall\\,v,w\\in V\\;\\bigl(\\sigma(v,w)=\\varphi(a(v),a(w))\\bigr)\\} \$ .

-   Изоморфизмы между пр.-вами с формой: \$ \\mathrm{Iso}((V,\\sigma),(Y,\\varphi))=\\mathrm{Hom}((V,\\sigma),(Y,\\varphi))\\cap\\mathrm{Bij}(V,Y) \$ и \$ (V,\\sigma)\\cong(Y,\\varphi)\\,\\Leftrightarrow\\,\\mathrm{Iso}((V,\\sigma),(Y,\\varphi))\\ne\\varnothing \$ .

##### 6.2  ¯-Квадратичные формы

-   Пространство ¯-квадратичных форм: \$ \\overline{\\mathrm{Quad}}(V)=\\{\\kappa\\in\\mathrm{Func}(V,K)\\mid\\exists\\,\\sigma\\in\\overline{\\mathrm{Bi}}(V)\\;\\forall\\,v\\in V\\;\\bigl(\\kappa(v)=\\sigma(v,v)\\bigr)\\} \$ . Утверждение: \$ \\kappa(c\\,v)=c\\,\\overline c\\,\\kappa(v) \$ .
-   ¯-Квадратичная форма \$ \\kappa \$ в коорд.: \$ \\kappa(v)=(v\^e)\^{\\scriptscriptstyle\\mathsf T}\\!\\cdot\\sigma\_{e,e}\\!\\cdot\\overline{v\^e}=\\sum\_{j_1=1}\^n\\sum\_{j_2=1}\^n\\sigma\_{j_1,j_2}v\^{j_1}\\overline{v\^{j_2}} \$ ; если \$ \\overline{\\phantom c}=\\mathrm{id}\_K \$ , то \$ \\kappa(v) \$ --- однор. многочлен степени \$ 2 \$ от \$ v\^1,\\ldots,v\^n \$ .
-   <span class="underline">Теорема о поляризации квадратичных форм.</span> *Пусть \$ K \$ --- поле, \$ \\mathrm{char}\\,K\\ne2 \$ и \$ V \$ --- векторное пространство над \$ K \$ ; тогда
    (1) для любых \$ \\kappa\\in\\mathrm{Quad}(V) \$ , обозначая через \$ \\,\\mathrm{pol}\_\\kappa \$ отображение \$ \\biggl(\\!\\begin{align}V\\times V&\\to K\\\\(v,w)&\\mapsto\\bigl(\\kappa(v+w)-\\kappa(v)-\\kappa(w)\\bigr)/2\\end{align}\\!\\biggr) \$ , имеем следующие факты:
    \$ \\mathrm{pol}\_\\kappa \$ --- симметричная билинейная форма (то есть \$ \\mathrm{pol}\_\\kappa\\!\\in\\mathrm{SBi}(V) \$ ), а также \$ \\forall\\,v\\in V\\;\\bigl(\\mathrm{pol}\_\\kappa(v,v)=\\kappa(v)\\bigr) \$ ;
    (2) линейные операторы \$ \\biggl(\\!\\begin{align}\\mathrm{SBi}(V)&\\to\\mathrm{Quad}(V)\\\\\\sigma&\\mapsto\\bigl(v\\mapsto\\sigma(v,v)\\bigr)\\!\\end{align}\\!\\biggr) \$ и \$ \\biggl(\\!\\begin{align}\\mathrm{Quad}(V)&\\to\\mathrm{SBi}(V)\\\\\\kappa&\\mapsto\\mathrm{pol}\_\\kappa\\end{align}\\!\\biggr) \$ --- взаимно обратные изоморфизмы векторных пространств.*
-   <span class="underline">Теорема о поляризации ¯-квадратичных форм над полем **C**.</span> *Пусть \$ V \$ --- векторное пространство над \$ \\,\\mathbb C \$ ; тогда
    (1) для любых \$ \\kappa\\in\\overline\\mathrm{Quad}(V) \$ , обозначая через \$ \\,\\mathrm{pol}\_\\kappa \$ отображение \$ \\biggl(\\!\\begin{align}V\\times V&\\to\\mathbb C\\\\(v,w)&\\mapsto\\bigl(\\kappa(v+w)+\\mathrm i\\,\\kappa(v+\\mathrm i\\,w)-\\kappa(v-w)-\\mathrm i\\,\\kappa(v-\\mathrm i\\,w)\\bigr)/4\\end{align}\\!\\biggr) \$ , имеем
    следующие факты: \$ \\mathrm{pol}\_\\kappa \$ --- полуторалинейная форма (то есть \$ \\mathrm{pol}\_\\kappa\\!\\in\\overline\\mathrm{Bi}(V) \$ ), а также \$ \\forall\\,v\\in V\\;\\bigl(\\mathrm{pol}\_\\kappa(v,v)=\\kappa(v)\\bigr) \$ ;
    (2) линейные операторы \$ \\biggl(\\!\\begin{align}\\overline{\\mathrm{Bi}}(V)&\\to\\overline{\\mathrm{Quad}}(V)\\\\\\sigma&\\mapsto\\bigl(v\\mapsto\\sigma(v,v)\\bigr)\\!\\end{align}\\!\\biggr) \$ и \$ \\biggl(\\!\\begin{align}\\overline\\mathrm{Quad}(V)&\\to\\overline\\mathrm{Bi}(V)\\\\\\kappa&\\mapsto\\mathrm{pol}\_\\kappa\\end{align}\\!\\biggr) \$ --- взаимно обратные изоморфизмы векторных пространств.*
-   Гиперповерхность втор. порядка (аффинная квадрика) в \$ V \$ : мн.-во вида \$ \\{v\\in V\\mid\\kappa(v)+2\\,\\lambda(v)+c=0\\} \$ , где \$ \\kappa\\in\\mathrm{Quad}(V)\\!\\setminus\\!\\{0\\} \$ , \$ \\lambda\\in V\^\* \$ и \$ c\\in K \$ .
-   Примеры аффинных квадрик. Утверждение: *пусть \$ s\\in\\mathrm{Mat}(n,K) \$ , \$ \\lambda\\in K_n \$ , \$ c\\in K \$ и \$ v\\in K\^n \$ ; тогда \$ \\,v\^{\\scriptscriptstyle\\mathsf T}\\!\\cdot s\\cdot v+2\\,\\lambda\\cdot v+c=\\Bigl(\\begin{smallmatrix}v\\\\1\\end{smallmatrix}\\Bigr)\^{\\!\\scriptscriptstyle\\mathsf T}\\!\\!\\cdot\\!\\Bigl(\\begin{smallmatrix}s&\\lambda\^{\\scriptscriptstyle\\mathsf T}\\\\\\lambda&c\\end{smallmatrix}\\Bigr)\\!\\cdot\\!\\Bigl(\\begin{smallmatrix}v\\\\1\\end{smallmatrix}\\Bigr) \$* .

##### 6.3  Музыкальные изоморфизмы и невырожденные ¯-билинейные формы

-   Оператор бемоль (опускание индекса): \$ \\biggl(\\!\\begin{align}\\flat\_\\sigma\\colon V&\\to\\overline V\^\*\\\\v&\\mapsto\\bigl(w\\mapsto\\sigma(v,w)\\bigr)\\!\\end{align}\\!\\biggr) \$ . Опускание индекса в координатах: \$ (\\flat\_\\sigma v)\_e=(v\^e)\^{\\scriptscriptstyle\\mathsf T}\\!\\cdot\\sigma\_{e,e} \$ и \$ (\\flat\_\\sigma v)\_j=\\sum\_{i=1}\^nv\^i\\,\\sigma\_{i,j} \$ .
-   Случай \$ \\dim V\<\\infty \$ : \$ \\bigl( \$ \$ \\sigma \$ невырождена \$ \\bigr) \$ \$ \\;\\Leftrightarrow\\; \$ \$ \\bigl( \$ \$ \\flat\_\\sigma \$ --- биекция \$ \\bigr) \$ \$ \\;\\Leftrightarrow\\; \$ \$ \\mathrm{Ker}\\,\\flat\_\\sigma\\!=\\{0\\} \$ . Ранг формы \$ \\sigma \$ : \$ \\mathrm{rk}(\\sigma)=\\dim\\mathrm{Im}\\,\\flat\_\\sigma \$ . Утверждение: \$ \\mathrm{rk}(\\sigma)=\\mathrm{rk}(\\sigma\_{e,e}) \$ .
-   Топологическая невырожденность ( \$ K=\\mathbb R \$ или \$ K=\\mathbb C \$ , \$ V \$ --- нормир. пр.-во, \$ \\sigma\\in\\overline{\\mathrm{Bi}}(V)\\cap\\mathrm C\^0\\!(V\\times V,K) \$ ): \$ \\biggl(\\!\\begin{align}\\flat\_\\sigma\\colon V&\\to\\overline V\^\*\\!\\!\\cap\\mathrm C\^0\\!(V,K)\\\\v&\\mapsto\\bigl(w\\mapsto\\sigma(v,w)\\bigr)\\!\\end{align}\\!\\biggr) \$ --- биекция.
-   Пример: \$ K=\\mathbb R \$ или \$ K=\\mathbb C \$ , \$ V=\\ell\^2_K=\\bigl\\{f\\in\\mathrm{Func}(\\mathbb N,K)\\mid\\sum\_{n=1}\^\\infty\|f_i\|\^2\\!\<\\infty\\bigr\\} \$ и \$ \\sigma\\,\\colon(f,g)\\mapsto\\sum\_{i=1}\^\\infty f_i\\overline{g_i} \$ ; тогда \$ \\sigma \$ топологически невырожд. (без док.-ва).
-   Оператор диез (подъем индекса): \$ \\sharp\^\\sigma\\!=\\flat\_\\sigma\^{-1} \$ ( \$ \\sigma \$ невырождена). Подъем индекса в коорд. ( \$ \\sigma\^{e,e}=(\\sigma\_{e,e}\^{-1})\^{\\scriptscriptstyle\\mathsf T} \$ ): \$ (\\sharp\^\\sigma\\lambda)\^e=\\sigma\^{e,e}\\!\\cdot(\\lambda_e)\^{\\scriptscriptstyle\\mathsf T} \$ и \$ (\\sharp\^\\sigma\\lambda)\^i=\\sum\_{j=1}\^n\\sigma\^{i,j}\\,\\lambda_j \$ .
-   <span class="underline">Теорема о базисах и невырожденных формах.</span> *Пусть \$ K \$ --- поле с инволюцией, \$ V \$ --- вект. простр.-во над \$ K \$ , \$ \\sigma\\in\\overline\\mathrm{Bi}(V) \$ , \$ m\\in\\mathbb N_0 \$ , \$ v_1,\\ldots,v_m\\in V \$ и
    \$ U=\\langle v_1,\\ldots,v_m\\rangle \$ ; тогда \$ \\sigma\_{(v_1,\\ldots,v_m),(v_1,\\ldots,v_m)}\\!\\in\\mathrm{GL}(m,K) \$ , если и только если \$ (v_1,\\ldots,v_m)\\in\\mathrm{OB}(U) \$ и форма \$ \\sigma\|\_{U\\times U} \$ невырождена.*
-   Ортогональные векторы ( \$ \\sigma\\in\\overline\\mathrm{SBi}(V)\\cup\\overline\\mathrm{ABi}(V) \$ ): \$ v\\perp w\\,\\Leftrightarrow\\,\\sigma(v,w)=0\\,\\Leftrightarrow\\,\\sigma(w,v)=0 \$ . Ортогональн. дополнение: \$ U\^\\perp\\!=\\{v\\in V\\mid U\\perp v\\}\\le V \$ .
-   <span class="underline">Теорема об ортогональном дополнении.</span> *Пусть \$ K \$ --- поле с инволюцией, \$ V \$ --- вект. простр.-во над \$ K \$ , \$ \\sigma\\in\\overline\\mathrm{SBi}(V)\\cup\\overline\\mathrm{ABi}(V) \$ и \$ U,W\\le V \$ ; тогда
    (1) \$ U\\subseteq U\^{\\perp\\perp} \$ , \$ U\\subseteq W\\,\\Rightarrow\\,W\^\\perp\\!\\subseteq U\^\\perp \$ , \$ (U+W)\^\\perp\\!=U\^\\perp\\!\\cap W\^\\perp \$ и \$ \\,U\^\\perp\\!+W\^\\perp\\!\\subseteq(U\\cap W)\^\\perp \$ ;
    (2) если \$ \\dim V\<\\infty \$ и форма \$ \\sigma \$ невырождена, то \$ \\dim U\^\\perp\\!=\\dim V-\\dim U \$ , а также \$ U=U\^{\\perp\\perp} \$ и \$ \\,U\^\\perp\\!+W\^\\perp\\!=(U\\cap W)\^\\perp \$ ;
    (3) \$ \\mathrm{Ker}\\bigl(\\flat\_{\\sigma\|\_{U\\times U}}\\!\\bigr)\\!=U\\cap U\^\\perp \$ и, если \$ \\dim U\<\\infty \$ , то \$ \\bigl( \$ форма \$ \\sigma\|\_{U\\times U} \$ невырождена \$ \\bigr) \$ \$ \\;\\Leftrightarrow\\;\\, \$ \$ U\\cap U\^\\perp\\!=\\{0\\} \$ ;
    (4) если форма \$ \\sigma\|\_{U\\times U} \$ невырождена, то \$ V=U\\oplus U\^\\perp \$ (и, значит, определен ортогональный проектор на \$ U \$ : \$ \\biggl(\\!\\begin{align}\\mathrm{proj}\_U\\colon V=U\\oplus U\^\\perp\\!&\\to V\\\\v=u+w&\\mapsto u\\end{align}\\!\\biggr) \$ ).*

##### 6.4  Диагонализация ¯-симметричных ¯-билинейных форм

-   Ортогональный базис: \$ e\\in\\mathrm{OOB}(V,\\sigma) \$ \$ \\;\\Leftrightarrow\\; \$ \$ \\bigl( \$ \$ \\sigma\_{e,e} \$ --- диагональная матрица \$ \\bigr) \$ . Форма \$ \\sigma \$ в ортогональн. коорд. ( \$ e\\in\\mathrm{OOB}(V,\\sigma) \$ ): \$ \\sigma(v,w)=\\sum\_{i=1}\^n\\sigma\_{i,i}\\,v\^i\\overline{w\^i} \$ .

-   Ортонормированный базис ( \$ K=\\mathbb R \$ или \$ K=\\mathbb C \$ ): \$ e\\in\\mathrm{OnOB}(V,\\sigma) \$ \$ \\;\\Leftrightarrow\\; \$ \$ \\bigl( \$ \$ \\sigma\_{e,e} \$ --- диагональная матрица с \$ 1,\\ldots,1,-1,\\ldots,-1,0,\\ldots,0 \$ на диагонали \$ \\bigr) \$ .

-   <span class="underline">Лемма о неизотропном векторе.</span> *Пусть \$ K \$ --- поле с инволюцией, \$ \\mathrm{char}\\,K\\ne2 \$ , \$ V \$ --- вект. пр. над \$ K \$ и \$ \\sigma\\in\\overline\\mathrm{SBi}(V)\\!\\setminus\\!\\{0\\} \$ ; тогда \$ \\exists\\,v\\in V\\;\\bigl(\\sigma(v,v)\\ne0\\bigr) \$ .*

-   Теорема Лагранжа. Матричная формулировка теоремы Лагранжа. Алгоритм приведения квадратичной формы к сумме квадратов с коэффициентами.

    <span class="underline">Теорема Лагранжа.</span> *Пусть \$ K \$ --- поле с инволюцией, \$ \\mathrm{char}\\,K\\ne2 \$ , \$ V \$ --- векторное пространство над \$ K \$ , \$ \\dim V\<\\infty \$ и \$ \\sigma\\in\\overline\\mathrm{SBi}(V) \$ ; тогда
    (1) в пространстве \$ V \$ существует ортогональный базис (то есть \$ \\mathrm{OOB}(V,\\sigma)\\ne\\varnothing \$ );
    (2) если \$ K=\\mathbb R \$ или \$ K=\\mathbb C \$ , то в пространстве \$ V \$ существует ортонормированный базис (то есть \$ \\mathrm{OnOB}(V,\\sigma)\\ne\\varnothing \$ ).*

    <span class="underline">Матричная формулировка теоремы Лагранжа.</span> *Пусть \$ K \$ --- поле с инволюцией, \$ \\mathrm{char}\\,K\\ne2 \$ , \$ n\\in\\mathbb N_0 \$ и \$ s\\in\\overline\\mathrm S\\mathrm{Mat}(n,K) \$ ; тогда
    (1) существует такая матрица \$ g\\in\\mathrm{GL}(n,K) \$ , что \$ g\^{\\scriptscriptstyle\\mathsf T}\\!\\cdot s\\cdot\\overline g \$ --- диагональная матрица;
    (2) если \$ K=\\mathbb R \$ или \$ K=\\mathbb C \$ , то сущ.-т такая матрица \$ g\\in\\mathrm{GL}(n,K) \$ , что \$ g\^{\\scriptscriptstyle\\mathsf T}\\!\\cdot s\\cdot\\overline g \$ --- диаг. матрица с \$ 1,\\ldots,1,-1,\\ldots,-1,0,\\ldots,0 \$ на диагонали.*

-   <span class="underline">Лемма об ортогональном проекторе.</span> *Пусть \$ K \$ --- поле с инволюцией, \$ V \$ --- вект. пр.-во над \$ K \$ , \$ \\sigma\\in\\overline\\mathrm{SBi}(V) \$ , \$ U\\le V \$ , \$ m=\\dim U\<\\infty \$ , \$ e\\in\\mathrm{OB}(U) \$ ,
    форма \$ \\sigma\|\_{U\\times U} \$ невырождена и \$ v\\in V \$ ; тогда \$ \\mathrm{proj}\_U(v)\^e=(\\sigma\|\_{U\\times U})\^{e,e}\\!\\cdot\\!\\biggl(\\begin{smallmatrix}\\sigma(v,e_1)\\\\\\vdots\\\\\\sigma(v,e_m)\\end{smallmatrix}\\biggr) \$ и, если \$ e\\in\\mathrm{OOB}(U,\\sigma\|\_{U\\times U}) \$ , то \$ \\mathrm{proj}\_U(v)=\\sum\_{i=1}\^m\\frac{\\sigma(v,e_i)}{\\sigma(e_i,e_i)}\\,e_i \$* .

-   <span class="underline">Лемма об определителе матрицы Грама.</span> *Пусть \$ K \$ --- поле с инволюцией, \$ V \$ --- векторное простр.-во над \$ K \$ , \$ \\sigma\\in\\overline\\mathrm{SBi}(V) \$ , \$ m\\in\\mathbb N \$ , \$ v_1,\\ldots,v_m\\in V \$ ,
    \$ U=\\langle v_1,\\ldots,v\_{m-1}\\rangle \$ , форма \$ \\sigma\|\_{U\\times U} \$ невырождена и \$ \\hat v_m=v_m-\\mathrm{proj}\_U(v_m) \$ ; тогда \$ \\det\\sigma\_{(v_1,\\ldots,v_m),(v_1,\\ldots,v_m)}=\\det\\sigma\_{(v_1,\\ldots,v\_{m-1}),(v_1,\\ldots,v\_{m-1})}\\cdot\\sigma(\\hat v_m,\\hat v_m) \$ .*

-   <span class="underline">Процесс ортогонализации Грама--Шмидта.</span> *Пусть \$ K \$ --- поле с инволюцией, \$ V \$ --- векторное пространство над \$ K \$ , \$ n=\\dim V\<\\infty \$ , \$ \\sigma\\in\\overline\\mathrm{SBi}(V) \$ и
    \$ e\\in\\mathrm{OB}(V) \$ ; для любых \$ i\\in\\{0,\\ldots,n\\} \$ обозначим через \$ V_i \$ пространство \$ \\langle e_1,\\ldots,e_i\\rangle \$ и обозначим через \$ cm_i \$ \$ i \$ -й угловой минор матрицы \$ \\sigma\_{e,e} \$ (то
    есть \$ cm_i=\\det\\sigma\_{(e_1,\\ldots,e_i),(e_1,\\ldots,e_i)} \$ ). Пусть для любых \$ i\\in\\{1,\\ldots,n-1\\} \$ форма \$ \\sigma\|\_{V_i\\times V_i} \$ невырождена (это эквивалентно тому, что \$ cm_i\\ne0 \$ ); для
    любых \$ i\\in\\{1,\\ldots,n\\} \$ обозначим через \$ \\hat e_i \$ вектор \$ e_i-\\mathrm{proj}\_{V\_{i-1}}(e_i) \$ . Тогда для любых \$ i\\in\\{1,\\ldots,n\\} \$ выполнено \$ (\\hat e_1,\\dots,\\hat e_i)\\in\\mathrm{OOB}(V_i,\\sigma\|\_{V_i\\times V_i}) \$ и
    \$ \\sigma(\\hat e_i,\\hat e_i)=\\frac{cm_i}{cm\_{i-1}} \$ , а также \$ \\hat e_i=e_i-\\sum\_{j=1}\^{i-1}\\frac{\\sigma(e_i,\\hat e_j)}{\\sigma(\\hat e_j,\\hat e_j)}\\,\\hat e_j \$ (это индуктивная формула для нахождения векторов \$ \\hat e_1,\\ldots,\\hat e_n \$ ).*

-   Ортогонал. системы функций: \$ \\cos(nx) \$ и \$ \\sin(nx) \$ ( \$ n\\in\\mathbb N \$ ), \$ \\mathrm e\^{nx\\,\\mathrm i} \$ ( \$ n\\in\\mathbb Z \$ ), многочлены Лежандра, Чебышёва, Эрмита (см. пункты 5--10 в § 4 части 2 в \[5\]).

### 7   Геометрия в векторных пространствах над \$ \\mathbb R \$ или \$ \\mathbb C \$

##### 7.1  Положительно и отрицательно определенные формы и сигнатура формы

-   Мн.-ва положительно и отрицательно определенных форм: \$ \\overline\\mathrm{SBi}\_{\>0}(V)=\\{\\sigma\\in\\overline\\mathrm{SBi}(V)\\mid\\forall\\,v\\in V\\!\\setminus\\!\\{0\\}\\;\\bigl(\\sigma(v,v)\>0\\bigr)\\} \$ и \$ \\overline\\mathrm{SBi}\_{\<0}(V)=-\\overline\\mathrm{SBi}\_{\>0}(V) \$ .
-   Мн.-ва полож. и отриц. опред. матриц: \$ \\overline\\mathrm S\\mathrm{Mat}\_{\>0}(n,K)=\\{s\\in\\overline\\mathrm S\\mathrm{Mat}(n,K)\\mid\\forall\\,v\\in K\^n\\!\\setminus\\!\\{0\\}\\;\\bigl(v\^{\\scriptscriptstyle\\mathsf T}\\!\\cdot s\\cdot\\overline v\>0\\bigr)\\} \$ и \$ \\overline\\mathrm S\\mathrm{Mat}\_{\<0}(n,K)=-\\overline\\mathrm S\\mathrm{Mat}\_{\>0}(n,K){} \$ .
-   <span class="underline">Следствия из теоремы об ортогональном дополнении и теоремы Лагранжа.</span> *Пусть \$ K=\\mathbb R \$ или \$ K=\\mathbb C \$ , \$ V \$ --- вект. пр.-во над \$ K \$ и \$ \\sigma\\in\\overline\\mathrm{Bi}(V) \$ ; тогда
    (1) если \$ \\sigma\\in\\overline\\mathrm{SBi}\_{\>0}(V) \$ и \$ U\\le V \$ , то \$ U\\cap U\^\\perp\\!=\\{0\\} \$ и, если \$ \\dim U\<\\infty \$ , то форма \$ \\sigma\|\_{U\\times U} \$ невырождена и \$ V=U\\oplus U\^\\perp \$ ;
    (2) если \$ n=\\dim V\<\\infty \$ , то \$ \\sigma\\in\\overline\\mathrm{SBi}\_{\>0}(V) \$ , если и только если \$ \\exists\\,e\\in\\mathrm{OB}(V)\\;\\bigl(\\sigma\_{e,e}=\\mathrm{id}\_n\\bigr) \$ ;
    (3) если \$ n=\\dim V\<\\infty \$ и \$ e\\in\\mathrm{OB}(V) \$ , то \$ \\sigma\\in\\overline\\mathrm{SBi}\_{\>0}(V) \$ , если и только если \$ \\exists\\,g\\in\\mathrm{GL}(n,K)\\;\\bigl(\\sigma\_{e,e}=g\^{\\scriptscriptstyle\\mathsf T}\\!\\cdot\\overline g\\bigr) \$ .*
-   <span class="underline">Критерий Сильвестра.</span> *Пусть \$ K=\\mathbb R \$ или \$ K=\\mathbb C \$ , \$ V \$ --- векторное пространство над \$ K \$ , \$ n=\\dim V\<\\infty \$ , \$ \\sigma\\in\\overline\\mathrm{SBi}(V) \$ и \$ e\\in\\mathrm{OB}(V) \$ ; для любых
    \$ i\\in\\{1,\\ldots,n\\} \$ обозначим через \$ cm_i \$ \$ i \$ -й угловой минор матрицы \$ \\sigma\_{e,e} \$ (то есть \$ cm_i=\\det\\sigma\_{(e_1,\\ldots,e_i),(e_1,\\ldots,e_i)} \$ ); тогда
    (1) \$ \\sigma\\in\\overline\\mathrm{SBi}\_{\>0}(V) \$ , если и только если \$ \\forall\\,i\\in\\{1,\\ldots,n\\}\\;\\bigl(cm_i\>0\\bigr) \$ ;
    (2) \$ \\sigma\\in\\overline\\mathrm{SBi}\_{\<0}(V) \$ , если и только если \$ \\forall\\,i\\in\\{1,\\ldots,n\\}\\;\\bigl((-1)\^i\\,cm_i\>0\\bigr) \$ .*
-   Индексы инерции формы \$ \\sigma \$ : \$ \\mathrm{ind}\_{\>0}(\\sigma)=\\max\\{\\dim U\\mid U\\le V\\,\\land\\,\\sigma\|\_{U\\times U}\\!\\in\\overline{\\mathrm{SBi}}\_{\>0}(U)\\} \$ и \$ \\mathrm{ind}\_{\<0}(\\sigma)=\\max\\{\\dim U\\mid U\\le V\\,\\land\\,\\sigma\|\_{U\\times U}\\!\\in\\overline{\\mathrm{SBi}}\_{\<0}(U)\\} \$ .
-   <span class="underline">Закон инерции Сильвестра.</span> *Пусть \$ K=\\mathbb R \$ или \$ K=\\mathbb C \$ , \$ V \$ --- векторное простр.-во над \$ K \$ , \$ n=\\dim V\<\\infty \$ , \$ \\sigma\\in\\overline\\mathrm{SBi}(V) \$ и \$ e\\in\\mathrm{OOB}(V,\\sigma) \$ ; тогда
    (1) \$ \\mathrm{ind}\_{\>0}(\\sigma)=\|\\{i\\in\\{1,\\ldots,n\\}\\mid\\sigma(e_i,e_i)\>0\\}\| \$ (и, значит, число \$ \|\\{i\\in\\{1,\\ldots,n\\}\\mid\\sigma(e_i,e_i)\>0\\}\| \$ не зависит от \$ e \$ );
    (2) \$ \\mathrm{ind}\_{\<0}(\\sigma)=\|\\{i\\in\\{1,\\ldots,n\\}\\mid\\sigma(e_i,e_i)\<0\\}\| \$ (и, значит, число \$ \|\\{i\\in\\{1,\\ldots,n\\}\\mid\\sigma(e_i,e_i)\<0\\}\| \$ не зависит от \$ e \$ );
    (3) \$ \\mathrm{ind}\_{\>0}(\\sigma)+\\mathrm{ind}\_{\<0}(\\sigma)=\\mathrm{rk}(\\sigma) \$ .*
-   <span class="underline">Теорема о классификации пространств с формой.</span> *Пусть \$ K=\\mathbb R \$ или \$ K=\\mathbb C \$ , \$ V,Y \$ --- вект. простр.-ва над \$ K \$ , \$ \\dim V,\\dim Y\<\\infty \$ , \$ \\sigma\\in\\overline\\mathrm{SBi}(V) \$ и
    \$ \\varphi\\in\\overline\\mathrm{SBi}(Y) \$ ; тогда \$ (V,\\sigma)\\cong(Y,\\varphi) \$ , если и только если \$ \\dim V=\\dim Y \$ , \$ \\mathrm{ind}\_{\>0}(\\sigma)=\\mathrm{ind}\_{\>0}(\\varphi) \$ и \$ \\mathrm{ind}\_{\<0}(\\sigma)=\\mathrm{ind}\_{\<0}(\\varphi) \$ .*
-   Сигнатура формы \$ \\sigma \$ : \$ (\\mathrm{ind}\_{\>0}(\\sigma),\\mathrm{ind}\_{\<0}(\\sigma)) \$ (или \$ \\mathrm{ind}\_{\>0}(\\sigma)-\\mathrm{ind}\_{\<0}(\\sigma) \$ ). Исследование кривых и поверхностей второго порядка (см. § 2 главы VIII в \[1\]).

##### 7.2  Предгильбертовы пространства

-   Предгильбертово пространство --- вект. пр.-во над \$ \\mathbb R \$ или \$ \\mathbb C \$ с полож. опред. формой. Обозн.-е формы: \$ (\\,\\mid\\,) \$ . Примеры: \$ (v\\!\\mid\\!w)=v\^{\\scriptscriptstyle\\mathsf T}\\!\\cdot\\overline w \$ , \$ (f\\!\\mid\\!g)=\\!\\int\_\\alpha\^\\beta\\!\\!f\\,\\overline g \$ .

-   Евклидово \$ \\,/\\, \$ унитарное пр.-во --- конечномерн. вект. пр.-во над \$ \\mathbb R \$ \$ \\,/\\, \$ \$ \\mathbb C \$ с полож. опред. формой, то есть конечномерн. предгильбертово пр.-во над \$ \\mathbb R \$ \$ \\,/\\, \$ \$ \\mathbb C \$ .

-   Норма: \$ \\\|v\\\|=\\sqrt{(v\\!\\mid\\!v)} \$ . Утверждение: *\$ v\\ne0\\,\\Rightarrow\\,\\\|v\\\|\>0 \$ и \$ \\\|c\\,v\\\|=\|c\|\\,\\\|v\\\| \$* . Гильбертово пространство --- полное предгильбертово пр.-во. Пример: \$ \\ell\^2 \$ .

-   <span class="underline">Теорема о свойствах нормы.</span> *Пусть \$ V \$ --- предгильбертово пространство; тогда
    (1) для любых \$ v,w\\in V \$ выполнено \$ \|(v\\!\\mid\\!w)\|\\le\\\|v\\\|\\,\\\|w\\\| \$ (это неравенство Коши--Буняковского--Шварца);
    (2) для любых \$ v,w\\in V \$ выполнено \$ \\\|v+w\\\|\\le\\\|v\\\|+\\\|w\\\| \$ (это неравенство треугольника);
    (3) если \$ \\dim V\<\\infty \$ , то для любых \$ e\\in\\mathrm{OnOB}(V) \$ и \$ v\\in V \$ выполнено \$ v=\\!\\sum\_{i=1}\^{\\dim V}\\!(v\\!\\mid\\!e_i)\\,e_i \$ и \$ \\\|v\\\|\^2=\\!\\sum\_{i=1}\^{\\dim V}\\!\|(v\\!\\mid\\!e_i)\|\^2 \$ (это равенство Парсеваля).*

-   Метрика: \$ \\mathrm{dist}(v,w)=\\\|v-w\\\| \$ . Расстояние между подмн.-вами: \$ \\mathrm{dist}(X,Y)=\\inf\\,\\{\\mathrm{dist}(x,y)\\mid x\\in X,\\,y\\in Y\\} \$ . Теорема о расстояниях и проекциях.

    <span class="underline">Теорема о расстояниях и проекциях.</span> *Пусть \$ V \$ --- предгильбертово пространство и \$ U,U\'\\!\\le V \$ ; тогда
    (1) для любых \$ v,v\'\\!\\in V \$ выполнено \$ \\mathrm{dist}(v+U,v\'+U\')=\\mathrm{dist}(v-v\',U+U\') \$ ;
    (2) если \$ \\dim U\<\\infty \$ , то для любых \$ v\\in V \$ выполнено \$ \\mathrm{dist}(v,U)=\\mathrm{dist}(v,\\mathrm{proj}\_U(v)) \$ ;
    (3) если \$ \\dim V\<\\infty \$ , то \$ \\mathrm{proj}\_U\\!+\\mathrm{proj}\_{U\^\\perp}\\!=\\mathrm{id}\_V \$ и для любых \$ v\\in V \$ выполнено \$ \\mathrm{dist}(v,U)=\\\|\\mathrm{proj}\_{U\^\\perp}\\!(v)\\\| \$ ;
    (4) если \$ \\dim U\<\\infty \$ , то для любых \$ e\\in\\mathrm{OnOB}(U) \$ и \$ v\\in V \$ выполнено \$ \\mathrm{proj}\_U(v)=\\!\\sum\_{i=1}\^{\\dim U}\\!(v\\!\\mid\\!e_i)\\,e_i \$ и \$ \\\|v\\\|\^2\\ge\\!\\sum\_{i=1}\^{\\dim U}\\!\|(v\\!\\mid\\!e_i)\|\^2 \$ (это неравенство Бесселя).*

-   Метод наименьших квадратов: замена системы \$ a\\cdot v=y \$ , где \$ a\\in\\mathrm{Mat}(p,n,\\mathbb R) \$ и \$ \\mathrm{rk}(a)=n \$ , на систему \$ a\\cdot v=\\mathrm{proj}\_X(y) \$ , где \$ X=\\{a\\cdot v\\mid v\\in\\mathbb R\^n\\} \$ .

-   Угол между векторами и между вектором и подпр.-вом ( \$ K=\\mathbb R \$ , \$ v\\ne0 \$ , \$ w\\ne0 \$ , \$ U\\ne\\{0\\} \$ ): \$ \\angle(v,w)=\\arccos\\frac{(v\\!\\mid\\!w)}{\\\|v\\\|\\,\\\|w\\\|}{} \$ и \$ \\angle(v,U)=\\arccos\\frac{\\\|\\mathrm{proj}\_U(v)\\\|}{\\\|v\\\|} \$ .

-   Псевдоевклидово \$ \\,/\\, \$ псевдоунитарное пр.-во сигнатуры \$ (p,q) \$ --- кон.-мерн. вект. пр.-во над \$ \\mathbb R \$ \$ \\,/\\, \$ \$ \\mathbb C \$ с невыр. ¯-симметр. ¯-билин. формой сигнатуры \$ (p,q) \$ .

##### 7.3  Ориентация, объем, векторное произведение

-   Отн.-е одинак. ориентированности ( \$ V \$ --- кон.-мерн. в. пр. над \$ \\mathbb R \$ , \$ e,\\tilde e\\in\\mathrm{OB}(V) \$ ): \$ e\\overset{\\scriptscriptstyle\\mathrm{or}}\\sim\\tilde e\\,\\Leftrightarrow\\,\\det\\mathrm c_e\^\\tilde e\\!\>0 \$ . Утверждение: \$ V\\ne\\{0\\}\\,\\Rightarrow\\,\|\\mathrm{OB}(V)/{\\overset{\\scriptscriptstyle\\mathrm{or}}\\sim}\|=2 \$ .

-   Ориентация пр.-ва \$ V \$ --- выбор эл.-та \$ \\mathrm{OB}\_{\>0}(V) \$ мн.-ва \$ \\mathrm{OB}(V)/\\overset{\\scriptscriptstyle\\mathrm{or}}\\sim \$ . Знак набора векторов: \$ \\mathrm{sign}(v_1,\\ldots,v_n) \$ . Теорема о знаке базиса и формах объема.

    <span class="underline">Теорема о знаке базиса и формах объема.</span> *Пусть \$ V \$ --- векторное простр.-во с ориентацией и \$ e\\in\\mathrm{OB}(V) \$ ; тогда для любых \$ \\tilde e\\in\\mathrm{OB}(V) \$ выполнено
    \$ \\mathrm{sign}(\\tilde e)\\,\\mathrm{vol}\^\\tilde e\\!=\|\\det\\mathrm c_e\^\\tilde e\|\\,\\mathrm{sign}(e)\\,\\mathrm{vol}\^e \$ , а также множество \$ \\mathrm{VF}\_{\>0}(V) \$ , равное \$ \\,\\mathbb R\_{\>0}\\,\\mathrm{sign}(e)\\,\\mathrm{vol}\^e \$ , не зависит от выбора упорядоченного базиса \$ e \$ .*

-   Каноническая форма объема в псевдоевкл. пр.-ве с ориентацией ( \$ e\\in\\mathrm{OB}(V) \$ ): \$ \\mathrm{vol}=\\mathrm{sign}(e)\\sqrt{\|\\det\\sigma\_{e,e}\|}\\,\\mathrm{vol}\^e \$ ; если \$ e\\in\\mathrm{OnOB}\_{\>0}(V) \$ , то \$ \\mathrm{vol}=\\mathrm{vol}\^e \$ .

-   Корректность опр.-я объема. Объем в коорд.: \$ \\mathrm{vol}(v_1,\\ldots,v_n)=\\mathrm{sign}(e)\\sqrt{\|\\det\\sigma\_{e,e}\|}\\!\\!\\!\\sum\_{1\\le j_1,\\ldots,j_n\\le n}\\!\\!\\!\\varepsilon\_{j_1,\\ldots,j_n}v_1\^{j_1}\\!\\cdot\\ldots\\cdot v_n\^{j_n} \$ . Лемма об объеме и матрице Грама.

    <span class="underline">Лемма об объеме и матрице Грама.</span> *Пусть \$ V \$ --- псевдоевклидово пространство сигнатуры \$ (p,q) \$ с ориентацией, \$ n=p+q \$ и \$ v_1,\\ldots,v_n\\in V \$ ; тогда
    (1) \$ \\mathrm{vol}(v_1,\\ldots,v_n)=\\mathrm{sign}(v_1,\\ldots,v_n)\\sqrt{\|\\det\\sigma\_{(v_1,\\ldots,v_n),(v_1,\\ldots,v_n)}\|} \$ ;
    (2) для любых \$ w_1,\\ldots,w_n\\in V \$ выполнено \$ \\mathrm{vol}(v_1,\\ldots,v_n)\\cdot\\mathrm{vol}(w_1,\\ldots,w_n)=(-1)\^q\\det\\sigma\_{(v_1,\\ldots,v_n),(w_1,\\ldots,w_n)} \$ .*

-   Неотриц. объем в евкл. пр.-ве: \$ \|\\mathrm{vol}\|\_m(v_1,\\ldots,v_m)=\|\\mathrm{vol}(v_1,\\ldots,v_m)\| \$ в \$ \\langle v_1,\\ldots,v_m\\rangle \$ , если \$ v_1,\\ldots,v_m \$ независимы; иначе \$ \|\\mathrm{vol}\|\_m(v_1,\\ldots,v_m)=0 \$ .

-   <span class="underline">Теорема о неотрицательном объеме в евклидовом пространстве.</span> *Пусть \$ V \$ --- евклидово пространство, \$ m\\in\\mathbb N_0 \$ и \$ v_1,\\ldots,v_m\\in V \$ ; тогда
    (1) \$ \|\\mathrm{vol}\|\_m(v_1,\\ldots,v_m)=\\sqrt{\\det\\sigma\_{(v_1,\\ldots,v_m),(v_1,\\ldots,v_m)}} \$ ;
    (2) если \$ m\\ge1 \$ и \$ \\hat v_m=v_m-\\mathrm{proj}\_{\\langle v_1,\\ldots,v\_{m-1}\\rangle}(v_m) \$ , то \$ \|\\mathrm{vol}\|\_m(v_1,\\ldots,v_m)=\|\\mathrm{vol}\|\_{m-1}(v_1,\\ldots,v\_{m-1})\\cdot\\\|\\hat v_m\\\| \$ .*

-   Вект. произв. в псевдоевкл. пр.-ве с ориент.: \$ v_1\\times\\ldots\\times v\_{n-1}=\\sharp\\,\\bigl(v_n\\!\\mapsto\\mathrm{vol}(v_1,\\ldots,v_n)\\bigr) \$ ( \$ \\Leftrightarrow\\,\\forall\\,v_n\\in V\\;\\bigl((v_1\\times\\ldots\\times v\_{n-1}\\!\\mid\\!v_n)=\\mathrm{vol}(v_1,\\ldots,v_n)\\bigr) \$ ).

-   Векторное произведение в коорд.: \$ (v_1\\times\\ldots\\times v\_{n-1})\^i=\\mathrm{sign}(e)\\sqrt{\|\\det\\sigma\_{e,e}\|}\\!\\!\\!\\sum\_{1\\le j_1,\\ldots,j_n\\le n}\\!\\!\\!\\sigma\^{i,j_n}\\varepsilon\_{j_1,\\ldots,j_n}v_1\^{j_1}\\!\\cdot\\ldots\\cdot v\_{n-1}\^{j\_{n-1}} \$ . Теорема о векторном произведении.

    <span class="underline">Теорема о векторном произведении.</span> *Пусть \$ V \$ --- псевдоевклидово пр.-во сигнатуры \$ (p,q) \$ с ориентацией, \$ n=p+q\\ge1 \$ и \$ v_1,\\ldots,v\_{n-1}\\in V \$ ; тогда
    (1) \$ v_1\\times\\ldots\\times v\_{n-1}\\in\\langle v_1,\\ldots,v\_{n-1}\\rangle\^\\perp \$ , а также \$ v_1\\times\\ldots\\times v\_{n-1}\\ne0 \$ , если и только если векторы \$ v_1,\\ldots,v\_{n-1} \$ независимы;
    (2) если \$ q=0 \$ , то \$ \\\|v_1\\times\\ldots\\times v\_{n-1}\\\|=\|\\mathrm{vol}\|\_{n-1}(v_1,\\ldots,v\_{n-1}) \$ и, если \$ v_1,\\ldots,v\_{n-1} \$ независимы, то \$ (v_1,\\ldots,v\_{n-1},v_1\\times\\ldots\\times v\_{n-1})\\in\\mathrm{OB}\_{\>0}(V) \$ ;
    (3) для любых \$ w_1,\\ldots,w\_{n-1}\\in V \$ выполнено \$ (v_1\\times\\ldots\\times v\_{n-1}\\!\\mid\\!w_1\\times\\ldots\\times w\_{n-1})=(-1)\^q\\det\\sigma\_{(v_1,\\ldots,v\_{n-1}),(w_1,\\ldots,w\_{n-1})} \$ ;
    (4) если \$ n=3 \$ и \$ q=0 \$ , то для любых \$ u,v,w\\in V \$ выполнено \$ (u\\times v)\\times w=(u\\!\\mid\\!w)\\,v-(v\\!\\mid\\!w)\\,u\\, \$ и \$ \\,(u\\times v)\\times w+(v\\times w)\\times u+(w\\times u)\\times v=0 \$ .*

##### 7.4  Автоморфизмы пространств с формой, ортогональные и унитарные операторы и матрицы

-   Группа автоморфизмов пр.-ва с ¯-билинейной формой: \$ \\mathrm{Aut}(V,\\sigma)=\\mathrm{Iso}((V,\\sigma),(V,\\sigma))=\\{a\\in\\mathrm{GL}(V)\\mid\\forall\\,v,w\\in V\\;\\bigl(\\sigma(a(v),a(w))=\\sigma(v,w)\\bigr)\\} \$ .
-   Утверждение: *пусть \$ \\mathrm{char}\\,K\\ne2 \$ и \$ \\sigma\\in\\mathrm{SBi}(V) \$ , или \$ K=\\mathbb C \$ и \$ \\sigma\\in\\overline\\mathrm{Bi}(V) \$ ; тогда \$ \\,\\mathrm{Aut}(V,\\sigma)=\\{a\\in\\mathrm{GL}(V)\\mid\\forall\\,v\\in V\\;\\bigl(\\sigma(a(v),a(v))=\\sigma(v,v)\\bigr)\\} \$* .
-   Ортогональная группа ( \$ V \$ --- в. пр. над \$ \\mathbb R \$ , \$ \\sigma\\in\\mathrm{SBi}(V) \$ ): \$ \\mathrm O(V)=\\mathrm{Aut}(V,\\sigma) \$ . Унитарная группа ( \$ V \$ --- в. пр. над \$ \\mathbb C \$ , \$ \\sigma\\in\\overline\\mathrm{SBi}(V) \$ ): \$ \\mathrm U(V)=\\mathrm{Aut}(V,\\sigma) \$ .
-   <span class="underline">Лемма об автоморфизмах пространств с формой и матрицах.</span>
    *(1) Пусть \$ K \$ --- поле с инволюцией, \$ V \$ --- векторное пространство над \$ K \$ , \$ n=\\dim V\<\\infty \$ , \$ \\sigma\\in\\overline\\mathrm{Bi}(V) \$ , \$ a\\in\\mathrm{End}(V) \$ и \$ e\\in\\mathrm{OB}(V) \$ ; тогда
    \$ a\\in\\mathrm{Aut}(V,\\sigma)\\,\\Leftrightarrow\\,a_e\^e\\in\\mathrm{GL}(n,K)\\,\\land\\,(a_e\^e)\^{\\scriptscriptstyle\\mathsf T}\\!\\cdot\\sigma\_{e,e}\\!\\cdot\\overline{a_e\^e}=\\sigma\_{e,e} \$ и, если форма \$ \\sigma \$ невырождена, то условие « \$ \\,a_e\^e\\in\\mathrm{GL}(n,K) \$ » можно убрать.
    (2) Пусть \$ V \$ --- псевдоевклидово пространство сигнатуры \$ (p,q) \$ и \$ e,\\tilde e\\in\\mathrm{OnOB}(V) \$ ; тогда \$ (\\mathrm c\_\\tilde e\^e)\^{\\scriptscriptstyle\\mathsf T}\\!\\cdot\\!\\Bigl(\\begin{smallmatrix}\\mathrm{id}\_p&0\\\\0&-\\mathrm{id}\_q\\end{smallmatrix}\\Bigr)\\!\\cdot\\mathrm c\_\\tilde e\^e=\\!\\Bigl(\\begin{smallmatrix}\\mathrm{id}\_p&0\\\\0&-\\mathrm{id}\_q\\end{smallmatrix}\\Bigr) \$ .
    (3) Пусть \$ V \$ --- псевдоунитарное пространство сигнатуры \$ (p,q) \$ и \$ e,\\tilde e\\in\\mathrm{OnOB}(V) \$ ; тогда \$ (\\mathrm c\_\\tilde e\^e)\^{\\scriptscriptstyle\\mathsf T}\\!\\cdot\\!\\Bigl(\\begin{smallmatrix}\\mathrm{id}\_p&0\\\\0&-\\mathrm{id}\_q\\end{smallmatrix}\\Bigr)\\!\\cdot\\overline{\\mathrm c\_\\tilde e\^e}=\\!\\Bigl(\\begin{smallmatrix}\\mathrm{id}\_p&0\\\\0&-\\mathrm{id}\_q\\end{smallmatrix}\\Bigr) \$ .*
-   Матричные ортогонал. группы: \$ \\mathrm O(p,q)=\\{a\\in\\mathrm{Mat}(p+q,\\mathbb R)\\mid a\^{\\scriptscriptstyle\\mathsf T}\\!\\cdot\\!\\Bigl(\\begin{smallmatrix}\\mathrm{id}\_p&0\\\\0&-\\mathrm{id}\_q\\end{smallmatrix}\\Bigr)\\!\\cdot a=\\!\\Bigl(\\begin{smallmatrix}\\mathrm{id}\_p&0\\\\0&-\\mathrm{id}\_q\\end{smallmatrix}\\Bigr)\\} \$ , \$ \\mathrm{SO}(p,q)=\\mathrm{SL}(p+q,\\mathbb R)\\cap\\mathrm O(p,q) \$ и \$ \\mathrm O(n) \$ , \$ \\mathrm{SO}(n) \$ .
-   Матричные унитарные группы: \$ \\mathrm U(p,q)=\\{a\\in\\mathrm{Mat}(p+q,\\mathbb C)\\mid a\^{\\scriptscriptstyle\\mathsf T}\\!\\cdot\\!\\Bigl(\\begin{smallmatrix}\\mathrm{id}\_p&0\\\\0&-\\mathrm{id}\_q\\end{smallmatrix}\\Bigr)\\!\\cdot\\overline a=\\!\\Bigl(\\begin{smallmatrix}\\mathrm{id}\_p&0\\\\0&-\\mathrm{id}\_q\\end{smallmatrix}\\Bigr)\\} \$ , \$ \\mathrm{SU}(p,q)=\\mathrm{SL}(p+q,\\mathbb C)\\cap\\mathrm U(p,q) \$ и \$ \\mathrm U(n) \$ , \$ \\mathrm{SU}(n) \$ .
-   Примеры: \$ \\mathrm{SO}(2)=\\bigl\\{\\Bigl(\\begin{smallmatrix}\\cos\\varphi&-{\\sin\\varphi}\\\\\\sin\\varphi&\\cos\\varphi\\end{smallmatrix}\\Bigr)\\!\\mid\\varphi\\in\[0;2\\pi)\\bigr\\} \$ , \$ \\mathrm O(2)=\\mathrm{SO}(2)\\cup\\bigl\\{\\Bigl(\\begin{smallmatrix}\\cos\\varphi&\\sin\\varphi\\\\\\sin\\varphi&-{\\cos\\varphi}\\end{smallmatrix}\\Bigr)\\!\\mid\\varphi\\in\[0;2\\pi)\\bigr\\} \$ и \$ \\mathrm{SU}(2)=\\bigl\\{\\Bigl(\\begin{smallmatrix}c&d\\\\-\\overline d&\\overline c\\end{smallmatrix}\\Bigr)\\!\\mid c,d\\in\\mathbb C,\\,\|c\|\^2\\!+\|d\|\^2\\!=1\\bigr\\} \$ .
-   <span class="underline">Теорема Эйлера о вращениях.</span> *Пусть \$ V \$ --- евклидово пр.-во с ориентацией, \$ \\dim V=3 \$ и \$ a\\in\\mathrm{SO}(V) \$ ; тогда существуют такие \$ e\\in\\mathrm{OnOB}\_{\>0}(V) \$ и
    \$ \\varphi\\in\[0;2\\pi) \$ , что \$ a_e\^e=\\biggl(\\begin{smallmatrix}1&0&0\\\\0&\\cos\\varphi&-{\\sin\\varphi}\\\\0&\\sin\\varphi&\\cos\\varphi\\end{smallmatrix}\\biggr) \$ (и, значит, \$ a \$ --- оператор поворота в \$ V \$ на угол \$ \\varphi \$ против часовой стрелки вокруг оси с напр. вектором \$ e_1 \$ ).*
-   Группа изометрий предгильбертова пр.-ва (как метрического пространства): \$ \\mathrm{Isom}(V)=\\{a\\in\\mathrm{Bij}(V)\\mid\\forall\\,v,w\\in V\\;\\bigl(\\mathrm{dist}(a(v),a(w))=\\mathrm{dist}(v,w)\\bigr)\\} \$ .
-   <span class="underline">Теорема об описании изометрий.</span> *Пусть \$ V \$ --- предгильбертово пространство над \$ \\,\\mathbb R \$ ; тогда \$ \\{a\\in\\mathrm{Isom}(V)\\mid a(0)=0\\}=\\mathrm O(V) \$ , а также, обозначая
    через \$ G \$ , \$ F \$ и \$ H \$ группу \$ \\,\\mathrm{Isom}(V) \$ и ее подгруппы \$ \\{\\bigl(v\\mapsto v+z\\bigr)\\!\\mid z\\in V\\} \$ и \$ \\{a\\in\\mathrm{Isom}(V)\\mid a(0)=0\\} \$ соответственно, имеем следующие факты:
    \$ F\\cap H=\\{\\mathrm{id}\_V\\} \$ , \$ G=F\\circ H \$ , \$ \\forall\\,h\\in H\\;\\bigl(h\\circ F\\circ h\^{-1}\\!\\subseteq F\\bigr) \$ и \$ F\\cong V\^+\\! \$ (и, значит, \$ \\mathrm{Isom}(V)=\\{\\bigl(v\\mapsto a(v)+z\\bigr)\\!\\mid a\\in\\mathrm O(V),\\,z\\in V\\}\\cong V\^+\\!\\leftthreetimes\\mathrm O(V) \$ ).*

##### 7.5  Тело кватернионов

-   Кольцо кватернионов: \$ \\mathbb H=\\{\\alpha+\\beta\\,\\mathrm i+\\gamma\\,\\mathrm j+\\delta\\,\\mathrm k\\mid\\alpha,\\beta,\\gamma,\\delta\\in\\mathbb R\\} \$ , где \$ \\mathrm i\^2=\\mathrm j\^2=\\mathrm k\^2=-1 \$ , а также \$ \\mathrm i\\,\\mathrm j=-\\mathrm j\\,\\mathrm i=\\mathrm k \$ , \$ \\mathrm j\\,\\mathrm k=-\\mathrm k\\,\\mathrm j=\\mathrm i \$ и \$ \\mathrm k\\,\\mathrm i=-\\mathrm i\\,\\mathrm k=\\mathrm j \$ .

-   Скалярная (вещественная) часть и векторная (мнимая) часть кватерниона: \$ \\mathrm{Re}(\\alpha+\\beta\\,\\mathrm i+\\gamma\\,\\mathrm j+\\delta\\,\\mathrm k)=\\alpha \$ и \$ \\mathrm{Im}(\\alpha+\\beta\\,\\mathrm i+\\gamma\\,\\mathrm j+\\delta\\,\\mathrm k)=\\beta\\,\\mathrm i+\\gamma\\,\\mathrm j+\\delta\\,\\mathrm k \$ .

-   Пр.-во чистых кватернионов: \$ \\mathbb H\_\\mathrm{vect}\\!=\\{v\\in\\mathbb H\\mid\\mathrm{Re}(v)=0\\} \$ . Скалярное произв.-е, векторное произв.-е, норма в \$ \\mathbb H\_\\mathrm{vect} \$ : \$ (v\\!\\mid\\!w) \$ , \$ v\\times w \$ , \$ \\\|v\\\|=\\sqrt{(v\\!\\mid\\!v)} \$ .

-   Утверждение: \$ \\forall\\,v,w\\in\\mathbb H\_\\mathrm{vect}\\,\\bigl(v\\,w=-(v\\!\\mid\\!w)+v\\times w\\;\\land\\;v\^2=-\\\|v\\\|\^2\\bigr) \$ . Сопряжение: \$ \\overline a=\\mathrm{Re}(a)-\\mathrm{Im}(a) \$ . Модуль: \$ \|a\|=\\sqrt{\\mathrm{Re}(a)\^2+\\\|\\mathrm{Im}(a)\\\|\^2} \$ .

-   <span class="underline">Теорема о свойствах кватернионов.</span>
    *(1) Для любых \$ a\\in\\mathbb H \$ выполнено \$ a\\,\\overline a=\\overline a\\,a=\|a\|\^2 \$ и, если \$ a\\ne0 \$ , то \$ a\^{-1}\\!=\\!\\frac{\\overline a}{\|a\|\^2} \$ (и, значит, \$ \\mathbb H \$ --- тело).
    (2) Для любых \$ a,b\\in\\mathbb H \$ выполнено \$ \\overline{a+b}=\\overline a+\\overline b \$ и \$ \\overline{a\\,b}=\\overline b\\,\\overline a \$ (и, значит, отображение \$ \\biggl(\\!\\begin{align}\\mathbb H&\\to\\mathbb H\\\\a&\\mapsto\\overline a\\end{align}\\!\\biggr) \$ --- антиавтоморфизм тела \$ \\,\\mathbb H \$ ).
    (3) Для любых \$ a,b\\in\\mathbb H \$ выполнено \$ \|a\\,b\|=\|a\|\\,\|b\| \$ (и, значит, отображение \$ \\biggl(\\!\\begin{align}\\mathbb H\^\\times\\!\\!&\\to\\mathbb R\_{\>0}\\!\\\\a&\\mapsto\|a\|\\end{align}\\!\\biggr) \$ --- гомоморфизм групп).*

-   Группа \$ \\mathrm S\^3 \$ : \$ \\mathrm S\^3\\!=\\{g\\in\\mathbb H\\mid\|g\|=1\\} \$ . Утверждение: \$ \\mathbb H\^\\times\\!\\cong\\mathbb R\_{\>0}\\!\\times\\mathrm S\^3 \$ . Экспонента от кватерниона \$ a \$ : \$ \\mathrm e\^a\\!=\\sum\_{k=0}\^\\infty\\frac1{k!}\\,a\^k \$ . Теорема о свойствах экспоненты.

    <span class="underline">Теорема о свойствах экспоненты.</span>
    *(1) Для любых \$ a,b\\in\\mathbb H \$ выполнено \$ a\\,b=b\\,a\\,\\Rightarrow\\,\\mathrm e\^{a+b}\\!=\\mathrm e\^a\\!\\cdot\\mathrm e\^b \$ , а также \$ \\mathrm e\^0\\!=1 \$ и \$ \\mathrm e\^{-a}\\!=(\\mathrm e\^a)\^{-1} \$ .
    (2) Для любых \$ \\varphi\\in\\mathbb R \$ и таких \$ u\\in\\mathbb H\_\\mathrm{vect} \$ , что \$ \\\|u\\\|=1 \$ , выполнено \$ \\mathrm e\^{\\varphi\\,u}\\!=\\cos\\varphi+\\sin\\varphi\\;u \$ (и, значит, \$ \\mathrm S\^3\\!=\\{\\mathrm e\^{\\varphi\\,u}\\!\\mid\\varphi\\in\[0;\\pi\],\\,u\\in\\mathbb H\_\\mathrm{vect},\\,\\\|u\\\|=1\\} \$ ).*

-   <span class="underline">Теорема об описании поворотов при помощи кватернионов.</span> *(1) Пусть \$ \\varphi\\in\\mathbb R \$ , \$ u\\in\\mathbb H\_\\mathrm{vect} \$ и \$ \\\|u\\\|=1 \$ ; тогда \$ \\biggl(\\!\\begin{align}\\mathbb H\_\\mathrm{vect}\\!&\\to\\mathbb H\_\\mathrm{vect}\\\\v&\\mapsto\\mathrm e\^{\\varphi\\,u}\\,v\\,\\mathrm e\^{-\\varphi\\,u}\\!\\end{align}\\!\\biggr) \$ --- оператор
    поворота в пространстве \$ \\,\\mathbb H\_\\mathrm{vect} \$ на угол \$ 2\\varphi \$ против часовой стрелки вокруг оси с направляющим вектором \$ u \$ .
    (2) Отображение \$ \\biggl(\\!\\begin{align}\\mathrm S\^3\\!/\\{1,-1\\}&\\to\\mathrm{SO}(\\mathbb H\_\\mathrm{vect})\\\\\\{g,-g\\}&\\mapsto\\bigl(v\\mapsto g\\,v\\,g\^{-1}\\bigr)\\!\\end{align}\\!\\biggr) \$ определено корректно и является изоморфизмом групп (и, значит, \$ \\mathrm S\^3\\!/\\{1,-1\\}\\cong\\mathrm{SO}(3) \$ ).*

### 8   Алгебры

##### 8.1  Определения и конструкции, связанные с алгебрами

-   \$ K \$ -Алгебра --- вект. пространство над \$ K \$ с билинейным умножением --- кольцо в широком смысле слова с «правильным» умножением на скаляры из \$ K \$ .

-   Примеры: \$ \\mathrm{Func}(X,K) \$ , \$ K\[x\] \$ , \$ K(x) \$ , \$ \\mathrm{Mat}(n,K) \$ , \$ \\mathrm{End}(V) \$ ; \$ \\mathbb R \$ -алгебры \$ \\mathbb C \$ , \$ \\mathbb H \$ , \$ \\mathrm C\^0\\!(X,\\mathbb R) \$ , \$ \\mathrm C\^\\infty\\!(M,\\mathbb R) \$ . Структурн. константы алгебры: \$ m\^i\_{j_1,j_2}\\!\\!=(e\_{j_1}e\_{j_2})\^i \$ .

-   Теорема Кэли для ассоциативных алгебр с \$ 1 \$ . Инъект. гомоморфизмы \$ \\mathbb R \$ -алгебр: \$ \\biggl(\\!\\begin{align}\\mathbb C&\\to\\mathrm{Mat}(2,\\mathbb R)\\,\\\\\\alpha+\\beta\\,\\mathrm i&\\mapsto\\!\\Bigl(\\begin{smallmatrix}\\alpha&-\\beta\\\\\\beta&\\alpha\\end{smallmatrix}\\Bigr)\\end{align}\\!\\biggr) \$ и \$ \\biggl(\\!\\begin{align}\\mathbb H&\\to\\mathrm{Mat}(2,\\mathbb C)\\\\\\alpha+\\beta\\,\\mathrm i+\\gamma\\,\\mathrm j+\\delta\\,\\mathrm k&\\mapsto\\!\\Bigl(\\begin{smallmatrix}\\alpha+\\beta\\,\\mathrm i&\\gamma+\\delta\\,\\mathrm i\\\\-\\gamma+\\delta\\,\\mathrm i&\\alpha-\\beta\\,\\mathrm i\\end{smallmatrix}\\Bigr)\\end{align}\\!\\biggr) \$ .

    <span class="underline">Теорема Кэли для ассоциативных алгебр с 1.</span> *Пусть \$ K \$ --- поле и \$ A \$ --- ассоциативная \$ K \$ -алгебра с \$ 1 \$ ; обозначим через \$ {}\_K\\!A \$ векторное пространство
    над \$ K \$ , получающееся из \$ A \$ при «забывании» умножения в этой алгебре, и для любых \$ a\\in A \$ обозначим через \$ \\mathrm{lm}\_a \$ отображение \$ \\biggl(\\!\\begin{align}A&\\to A\\\\b&\\mapsto a\\,b\\end{align}\\!\\biggr) \$ ; тогда
    отобр. \$ \\biggl(\\!\\begin{align}A&\\to\\mathrm{End}({}\_K\\!A)\\\\a&\\mapsto\\mathrm{lm}\_a\\end{align}\\!\\biggr) \$ определено корректно и является инъективным гомоморфизмом алгебр с \$ 1 \$ (и, значит, \$ A\\cong\\{\\mathrm{lm}\_a\\!\\mid a\\in A\\}\\le\\mathrm{End}({}\_K\\!A) \$ ).*

-   Алгебра с делением: \$ \\forall\\,a\\in A\\!\\setminus\\!\\{0\\}\\;\\bigl(\\mathrm{lm}\_a,\\mathrm{rm}\_a\\!\\in\\mathrm{Bij}(A)\\bigr) \$ и \$ A\\ne\\{0\\} \$ . Примеры: \$ K \$ , \$ K(x) \$ ; \$ \\mathbb R \$ -алгебры с делением \$ \\mathbb C \$ , \$ \\mathbb H \$ , алгебра октонионов (октав) \$ \\mathbb O \$ .

-   Моноидная алгебра ( \$ M \$ --- моноид): \$ K\[M\]=\\mathrm{FinFunc}(M,K) \$ ; общий вид эл.-та: \$ \\sum\_{m\\in M}p_mm \$ ( \$ \|\\{m\\in M\\mid p_m\\ne0\\}\|\<\\infty \$ ); умнож.-е в \$ K\[M\] \$ : свертка.

-   Алгебра многочленов от свободных (некоммутирующих) перем.: \$ K\\langle x_1,\\ldots,x_n\\rangle=K\[\\mathrm W(x_1,\\ldots,x_n)\] \$ . Степень многочлена. Однородные многочлены.

-   Алгебра многочленов от коммутирующих переменных: \$ K\[x_1,\\ldots,x_n\]=K\[\\mathrm W(x_1,\\ldots,x_n)\^\\mathsf{ab}\]\\cong K\\langle x_1,\\ldots,x_n\\rangle/\\bigl(\\{x_ix_j-x_jx_i\\!\\mid i,j\\in\\{1,\\ldots,n\\}\\}\\bigr) \$ .

-   Алгебра многочленов от антикоммут. (грассмановых) перем.: \$ K\_\\wedge\[x_1,\\ldots,x_n\]=K\\langle x_1,\\ldots,x_n\\rangle/\\bigl(\\{x_ix_j+x_jx_i\\!\\mid i,j\\in\\{1,\\ldots,n\\}\\}\\cup\\{x_1\^2,\\ldots,x_n\^2\\}\\bigr) \$ .

##### 8.2  Алгебры Ли (основные определения и примеры)

-   \$ K \$ -Алгебра Ли --- \$ K \$ -алгебра, умножение в которой антисимметрично ( \$ \[a,a\]=0 \$ ) и удовлетв.-т тождеству Якоби ( \$ \[\[a,b\],c\]+\[\[b,c\],a\]+\[\[c,a\],b\]=0 \$ ).

-   Коммутатор эл.-тов ассоциативной алгебры: \$ \[a,b\]=a\\,b-b\\,a \$ . Алгебра \$ A\^{(-)} \$ : вект. простр.-во \$ {}\_K\\!A \$ с операцией \$ \[\\,,\] \$ . Утверждение: *\$ A\^{(-)} \$ --- алгебра Ли*.

-   Примеры: \$ \\mathfrak{gl}(V)=\\mathrm{End}(V)\^{(-)} \$ , \$ \\mathfrak{sl}(V)=\\{a\\in\\mathfrak{gl}(V)\\mid\\mathrm{tr}\\,a=0\\} \$ , трехмерное евклид. пр.-во с ориент. относ.-но \$ \\times \$ , \$ \\mathbb H\_\\mathrm{vect} \$ --- подалгебра алгебры \$ \\mathbb H\^{(-)} \$ .

-   Матричные алгебры Ли: \$ \\mathfrak{gl}(n,K) \$ , \$ \\mathfrak{sl}(n,K) \$ , \$ \\mathfrak o(n)=\\mathfrak{so}(n)=\\{a\\in\\mathfrak{gl}(n,\\mathbb R)\\mid a\^{\\scriptscriptstyle\\mathsf T}\\!=-a\\} \$ , \$ \\mathfrak u(n)=\\{a\\in\\mathfrak{gl}(n,\\mathbb C)\\mid a\^{\\scriptscriptstyle\\mathsf T}\\!=-\\overline a\\} \$ , \$ \\mathfrak{su}(n)=\\mathfrak{sl}(n,\\mathbb C)\\cap\\mathfrak u(n){} \$ .

-   <span class="underline">Теорема о группах матриц и матричных алгебрах Ли.</span> *Пусть \$ K=\\mathbb R \$ или \$ K=\\mathbb C \$ и \$ n\\in\\mathbb N_0 \$ ; для любых \$ G\\le\\mathrm{GL}(n,K) \$ обозначим через \$ \\,\\mathrm T\_{\\mathrm{id}\_n}G \$ мн.-во
    \$ \\{\\dot\\gamma(0)\\mid\\alpha\\in\[-\\infty;0),\\,\\beta\\in(0;\\infty\],\\,\\gamma\\in\\mathrm C\^\\infty\\!((\\alpha;\\beta),\\mathrm{Mat}(n,K)),\\,\\mathrm{Im}\\,\\gamma\\subseteq G,\\,\\gamma(0)=\\mathrm{id}\_n\\} \$ (это касательное пр.-во к группе \$ G \$ в точке \$ \\,\\mathrm{id}\_n \$ ); тогда
    \$ \\mathrm T\_{\\mathrm{id}\_n}\\mathrm{GL}(n,K)=\\mathfrak{gl}(n,K) \$ и \$ \\,\\mathrm T\_{\\mathrm{id}\_n}\\mathrm{SL}(n,K)=\\mathfrak{sl}(n,K) \$ , а также \$ \\,\\mathrm T\_{\\mathrm{id}\_n}\\mathrm O(n)=\\mathrm T\_{\\mathrm{id}\_n}\\mathrm{SO}(n)=\\mathfrak{so}(n) \$ , \$ \\mathrm T\_{\\mathrm{id}\_n}\\mathrm U(n)=\\mathfrak u(n) \$ и \$ \\,\\mathrm T\_{\\mathrm{id}\_n}\\mathrm{SU}(n)=\\mathfrak{su}(n) \$ .*

-   Теорема Кэли для алгебр Ли. Изоморфизмы \$ \\mathbb R \$ -алгебр Ли: \$ \\Biggl(\\!\\begin{align}\\mathbb R\^3\\!&\\to\\mathfrak{so}(3)\\\\\\biggl(\\begin{smallmatrix}\\beta\\\\\\gamma\\\\\\delta\\end{smallmatrix}\\biggr)\\!&\\mapsto\\!\\biggl(\\begin{smallmatrix}0&-\\delta&\\gamma\\\\\\delta&0&-\\beta\\\\-\\gamma&\\beta&0\\end{smallmatrix}\\biggr)\\end{align}\\!\\Biggr) \$ , \$ \\Biggl(\\!\\begin{align}\\mathbb R\^3\\!&\\to\\mathbb H\_\\mathrm{vect}\\\\\\biggl(\\begin{smallmatrix}\\beta\\\\\\gamma\\\\\\delta\\end{smallmatrix}\\biggr)\\!&\\mapsto{\\textstyle\\frac12}(\\beta\\,\\mathrm i+\\gamma\\,\\mathrm j+\\delta\\,\\mathrm k)\\end{align}\\!\\Biggr) \$ и \$ \\Biggl(\\!\\begin{align}\\mathbb R\^3\\!&\\to\\mathfrak{su}(2)\\\\\\biggl(\\begin{smallmatrix}\\beta\\\\\\gamma\\\\\\delta\\end{smallmatrix}\\biggr)\\!&\\mapsto{\\textstyle\\frac12}\\Bigl(\\begin{smallmatrix}\\beta\\,\\mathrm i&\\gamma+\\delta\\,\\mathrm i\\\\-\\gamma+\\delta\\,\\mathrm i&-\\beta\\,\\mathrm i\\end{smallmatrix}\\Bigr)\\end{align}\\!\\Biggr) \$ .

    <span class="underline">Теорема Кэли для алгебр Ли.</span> *Пусть \$ K \$ --- поле и \$ \\mathfrak g \$ --- \$ K \$ -алгебра Ли; обозначим через \$ {}\_K\\mathfrak g \$ векторное пространство над \$ K \$ , получающееся из \$ \\mathfrak g \$ при
    «забывании» умножения в этой алгебре, и для любых \$ a\\in\\mathfrak g \$ обозначим через \$ \\mathrm{ad}\_a \$ отображение \$ \\biggl(\\!\\begin{align}\\mathfrak g&\\to\\mathfrak g\\\\b&\\mapsto\[a,b\]\\end{align}\\!\\biggr) \$ ; тогда отображение \$ \\biggl(\\!\\begin{align}\\mathfrak g&\\to\\mathfrak{gl}({}\_K\\mathfrak g)\\\\a&\\mapsto\\mathrm{ad}\_a\\end{align}\\!\\biggr) \$
    определено корректно и является гомоморфизмом алгебр Ли.*

-   Алгебра Ли дифференцирований \$ K \$ -алгебры \$ A \$ : \$ \\mathrm{Der}(A)=\\{d\\in\\mathfrak{gl}({}\_K\\!A)\\mid\\forall\\,a,b\\in A\\;\\bigl(d(a\\,b)=d(a)\\,b+a\\,d(b)\\bigr)\\} \$ --- подалгебра алгебры \$ \\mathfrak{gl}({}\_K\\!A) \$ .

-   Дифференциров.-е (производная Ли) по вект. полю ( \$ M \$ --- откр. мн.-во в \$ \\mathbb R\^n \$ , \$ A=\\mathrm C\^\\infty\\!(M,\\mathbb R) \$ , \$ v\\in\\mathrm C\^\\infty\\!(M,\\mathbb R\^n) \$ ): \$ \\biggl(\\begin{align}\\mathcal L_v\\colon A&\\to A\\\\f&\\mapsto\\textstyle\\sum\_{i=1}\^nv\^i\\frac{\\partial f}{\\partial x\^i}\\end{align}\\!\\biggr)\\!\\in\\mathrm{Der}(A) \$ .
