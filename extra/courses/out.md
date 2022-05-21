## Подробный план четвертого модуля курса алгебры

### 6   Векторные пространства с ¯-билинейной формой

##### 6.1  ¯-Билинейные формы

-   Пр.-во билинейных форм: $ \rm{Bi}(V) $ . Примеры билин. форм: $ (v,w)\mapsto v^{\scriptscriptstyle\mathsf T} \cdot s\cdot w $ ( $ V=K^n $ , $ s\in\rm{Mat}(n,K) $ ), $ (f,g)\mapsto \int\_\alpha^\beta  sfg $ ( $ V=\rm C^0 ([\alpha;\beta],\mathbb R) $ , $ s\in V $ ).

-   Поля с инволюцией. Пространство $ \overline V $ : $ c\overline\cdot v=\overline c\,v $ . Пространство ¯-билинейн. форм (полуторалинейных форм, если $ \overline{\phantom c}\ne\rm{id}\_K $ ): $ \overline\rm{Bi}(V)=\rm{Bi}(V,\overline V,K) $ .

-   Матрица Грама формы $ \sigma $ : $ {(\sigma\_{e,e})}\_{j\_1,j\_2} =\sigma(e\_{j\_1} ,e\_{j\_2}) $ . Обобщенная матрица Грама: $ (\sigma\_{(v\_1,\ldots,v\_m),(w\_1,\ldots,w\_m)})\_{j\_1,j\_2} =\sigma(v\_{j\_1} ,w\_{j\_2}) $ . Теорема о матрице Грама.

    **Теорема о матрице Грама.** *Пусть $ K $ — поле с инволюцией, $ V $ — векторное простр.-во над $ K $ , $ n=\dim V<\infty $ , $ \sigma\in\overline\rm{Bi}(V) $ и $ e\in\rm{OB}(V) $ ; тогда
    (1) для любых $ v,w\in V $ выполнено $ \sigma(v,w)=(v^e)^{\scriptscriptstyle\mathsf T} \cdot\sigma\_{e,e} \cdot\overline{w^e}=\sum\_{j\_1=1}^n\sum\_{j\_2=1}^n\sigma\_{j\_1,j\_2}v^{j\_1}\overline{w^{j\_2}} $ (координаты вычисляются относительно $ e $ );
    (2) для любых $ m\in\mathbb N\_0 $ и $ v\_1,\ldots,v\_m,w\_1,\ldots,w\_m\in V $ выполнено $ \sigma\_{(v\_1,\ldots,v\_m),(w\_1,\ldots,w\_m)} =\bigl(v\_1^e\;\ldots\;v\_m^e\bigr)^{\scriptscriptstyle\mathsf T} \cdot\sigma\_{e,e} \cdot\overline{\bigl(w\_1^e\;\ldots\;w\_m^e\bigr)} $ .*

-   Изоморфизм вект. пр.-в $ \biggl( \begin{align}\overline\rm{Bi}(V)&\to\rm{Mat}(n,K)\\\sigma&\mapsto\sigma\_{e,e}\end{align} \biggr) $ . Преобразования при замене базиса: $ \sigma\_{\tilde e,\tilde e}=(\rm c\_\tilde e^e)^{\scriptscriptstyle\mathsf T} \cdot\sigma\_{e,e} \cdot\overline{\rm c\_\tilde e^e} $ и $ \sigma\_{\tilde{j\_1},\tilde{j\_2}} =\sum\_{l\_1=1}^n\sum\_{l\_2=1}^n(e\_\tilde{j\_1})^{l\_1}\overline{(e\_\tilde{j\_2})^{l\_2}}\,\sigma\_{l\_1,l\_2} $ .

-   Простр.-ва ¯-симметричных форм и матриц: $ \rm{\overline {SBi}}(V)=\{\sigma\in\overline\rm{Bi}(V)\mid\forall\,v,w\in V\;\bigl(\sigma(w,v)=\overline{\sigma(v,w)}\bigr)\} $ и $ \overline\rm S\rm{Mat}(n,K)=\{s\in\rm{Mat}(n,K)\mid s^{\scriptscriptstyle\mathsf T} =\overline s\} $ .

-   Пр.-ва ¯-антисимметр. форм и матриц: $ \overline\rm{ABi}(V)=\{\sigma\in\overline\rm{Bi}(V)\mid\forall\,v,w\in V\;\bigl(\sigma(w,v)=-\overline{\sigma(v,w)}\bigr)\} $ и $ \overline\rm A\rm{Mat}(n,K)=\{s\in\rm{Mat}(n,K)\mid s^{\scriptscriptstyle\mathsf T} =-\overline s\} $ .

-   Гомоморфизмы между простр.-вами с ¯-билинейной формой: $ \rm{Hom}((V,\sigma),(Y,\varphi))=\{a\in\rm{Hom}(V,Y)\mid\forall\,v,w\in V\;\bigl(\sigma(v,w)=\varphi(a(v),a(w))\bigr)\} $ .

-   Изоморфизмы между пр.-вами с формой: $ \rm{Iso}((V,\sigma),(Y,\varphi))=\rm{Hom}((V,\sigma),(Y,\varphi))\cap\rm{Bij}(V,Y) $ и $ (V,\sigma)\cong(Y,\varphi)\,\Leftrightarrow\,\rm{Iso}((V,\sigma),(Y,\varphi))\ne\varnothing $ .

##### 6.2  ¯-Квадратичные формы

-   Пространство ¯-квадратичных форм: $ \overline{\rm{Quad}}(V)=\{\kappa\in\rm{Func}(V,K)\mid\exists\,\sigma\in\overline{\rm{Bi}}(V)\;\forall\,v\in V\;\bigl(\kappa(v)=\sigma(v,v)\bigr)\} $ . Утверждение: $ \kappa(c\,v)=c\,\overline c\,\kappa(v) $ .
-   ¯-Квадратичная форма $ \kappa $ в коорд.: $ \kappa(v)=(v^e)^{\scriptscriptstyle\mathsf T} \cdot\sigma\_{e,e} \cdot\overline{v^e}=\sum\_{j\_1=1}^n\sum\_{j\_2=1}^n\sigma\_{j\_1,j\_2}v^{j\_1}\overline{v^{j\_2}} $ ; если $ \overline{\phantom c}=\rm{id}\_K $ , то $ \kappa(v) $ — однор. многочлен степени $ 2 $ от $ v^1,\ldots,v^n $ .
-   **Теорема о поляризации квадратичных форм.** *Пусть $ K $ — поле, $ \rm{char}\,K\ne2 $ и $ V $ — векторное пространство над $ K $ ; тогда
    (1) для любых $ \kappa\in\rm{Quad}(V) $ , обозначая через $ \,\rm{pol}\_\kappa $ отображение $ \biggl( \begin{align}V\times V&\to K\\(v,w)&\mapsto\bigl(\kappa(v+w)-\kappa(v)-\kappa(w)\bigr)/2\end{align} \biggr) $ , имеем следующие факты:
    $ \rm{pol}\_\kappa $ — симметричная билинейная форма (то есть $ \rm{pol}\_\kappa \in\rm{SBi}(V) $ ), а также $ \forall\,v\in V\;\bigl(\rm{pol}\_\kappa(v,v)=\kappa(v)\bigr) $ ;
    (2) линейные операторы $ \biggl( \begin{align}\rm{SBi}(V)&\to\rm{Quad}(V)\\\sigma&\mapsto\bigl(v\mapsto\sigma(v,v)\bigr) \end{align} \biggr) $ и $ \biggl( \begin{align}\rm{Quad}(V)&\to\rm{SBi}(V)\\\kappa&\mapsto\rm{pol}\_\kappa\end{align} \biggr) $ — взаимно обратные изоморфизмы векторных пространств.*
-   **Теорема о поляризации ¯-квадратичных форм над полем **C**.** *Пусть $ V $ — векторное пространство над $ \,\mathbb C $ ; тогда
    (1) для любых $ \kappa\in\overline\rm{Quad}(V) $ , обозначая через $ \,\rm{pol}\_\kappa $ отображение $ \biggl( \begin{align}V\times V&\to\mathbb C\\(v,w)&\mapsto\bigl(\kappa(v+w)+\rm i\,\kappa(v+\rm i\,w)-\kappa(v-w)-\rm i\,\kappa(v-\rm i\,w)\bigr)/4\end{align} \biggr) $ , имеем
    следующие факты: $ \rm{pol}\_\kappa $ — полуторалинейная форма (то есть $ \rm{pol}\_\kappa \in\overline\rm{Bi}(V) $ ), а также $ \forall\,v\in V\;\bigl(\rm{pol}\_\kappa(v,v)=\kappa(v)\bigr) $ ;
    (2) линейные операторы $ \biggl( \begin{align}\overline{\rm{Bi}}(V)&\to\overline{\rm{Quad}}(V)\\\sigma&\mapsto\bigl(v\mapsto\sigma(v,v)\bigr) \end{align} \biggr) $ и $ \biggl( \begin{align}\overline\rm{Quad}(V)&\to\overline\rm{Bi}(V)\\\kappa&\mapsto\rm{pol}\_\kappa\end{align} \biggr) $ — взаимно обратные изоморфизмы векторных пространств.*
-   Гиперповерхность втор. порядка (аффинная квадрика) в $ V $ : мн.-во вида $ \{v\in V\mid\kappa(v)+2\,\lambda(v)+c=0\} $ , где $ \kappa\in\rm{Quad}(V) \setminus \{0\} $ , $ \lambda\in V^* $ и $ c\in K $ .
-   Примеры аффинных квадрик. Утверждение: *пусть $ s\in\rm{Mat}(n,K) $ , $ \lambda\in K\_n $ , $ c\in K $ и $ v\in K^n $ ; тогда $ \,v^{\scriptscriptstyle\mathsf T} \cdot s\cdot v+2\,\lambda\cdot v+c=\Bigl(\begin{smallmatrix}v\\1\end{smallmatrix}\Bigr)^{ \scriptscriptstyle\mathsf T}  \cdot \Bigl(\begin{smallmatrix}s&\lambda^{\scriptscriptstyle\mathsf T}\\\lambda&c\end{smallmatrix}\Bigr) \cdot \Bigl(\begin{smallmatrix}v\\1\end{smallmatrix}\Bigr) $* .

##### 6.3  Музыкальные изоморфизмы и невырожденные ¯-билинейные формы

-   Оператор бемоль (опускание индекса): $ \biggl( \begin{align}\flat\_\sigma\colon V&\to\overline V^*\\v&\mapsto\bigl(w\mapsto\sigma(v,w)\bigr) \end{align} \biggr) $ . Опускание индекса в координатах: $ (\flat\_\sigma v)\_e=(v^e)^{\scriptscriptstyle\mathsf T} \cdot\sigma\_{e,e} $ и $ (\flat\_\sigma v)\_j=\sum\_{i=1}^nv^i\,\sigma\_{i,j} $ .
-   Случай $ \dim V<\infty $ : $ \bigl( $ $ \sigma $ невырождена $ \bigr) $ $ \;\Leftrightarrow\; $ $ \bigl( $ $ \flat\_\sigma $ — биекция $ \bigr) $ $ \;\Leftrightarrow\; $ $ \rm{Ker}\,\flat\_\sigma =\{0\} $ . Ранг формы $ \sigma $ : $ \rm{rk}(\sigma)=\dim\rm{Im}\,\flat\_\sigma $ . Утверждение: $ \rm{rk}(\sigma)=\rm{rk}(\sigma\_{e,e}) $ .
-   Топологическая невырожденность ( $ K=\mathbb R $ или $ K=\mathbb C $ , $ V $ — нормир. пр.-во, $ \sigma\in\overline{\rm{Bi}}(V)\cap\rm C^0 (V\times V,K) $ ): $ \biggl( \begin{align}\flat\_\sigma\colon V&\to\overline V^*  \cap\rm C^0 (V,K)\\v&\mapsto\bigl(w\mapsto\sigma(v,w)\bigr) \end{align} \biggr) $ — биекция.
-   Пример: $ K=\mathbb R $ или $ K=\mathbb C $ , $ V=\ell^2\_K=\bigl\{f\in\rm{Func}(\mathbb N,K)\mid\sum\_{n=1}^\infty\|f\_i\|^2 <\infty\bigr\} $ и $ \sigma\,\colon(f,g)\mapsto\sum\_{i=1}^\infty f\_i\overline{g\_i} $ ; тогда $ \sigma $ топологически невырожд. (без док.-ва).
-   Оператор диез (подъем индекса): $ \sharp^\sigma =\flat\_\sigma^{-1} $ ( $ \sigma $ невырождена). Подъем индекса в коорд. ( $ \sigma^{e,e}=(\sigma\_{e,e}^{-1})^{\scriptscriptstyle\mathsf T} $ ): $ (\sharp^\sigma\lambda)^e=\sigma^{e,e} \cdot(\lambda\_e)^{\scriptscriptstyle\mathsf T} $ и $ (\sharp^\sigma\lambda)^i=\sum\_{j=1}^n\sigma^{i,j}\,\lambda\_j $ .
-   **Теорема о базисах и невырожденных формах.** *Пусть $ K $ — поле с инволюцией, $ V $ — вект. простр.-во над $ K $ , $ \sigma\in\overline\rm{Bi}(V) $ , $ m\in\mathbb N\_0 $ , $ v\_1,\ldots,v\_m\in V $ и
    $ U=\langle v\_1,\ldots,v\_m\rangle $ ; тогда $ \sigma\_{(v\_1,\ldots,v\_m),(v\_1,\ldots,v\_m)} \in\rm{GL}(m,K) $ , если и только если $ (v\_1,\ldots,v\_m)\in\rm{OB}(U) $ и форма $ \sigma\|\_{U\times U} $ невырождена.*
-   Ортогональные векторы ( $ \sigma\in\overline\rm{SBi}(V)\cup\overline\rm{ABi}(V) $ ): $ v\perp w\,\Leftrightarrow\,\sigma(v,w)=0\,\Leftrightarrow\,\sigma(w,v)=0 $ . Ортогональн. дополнение: $ U^\perp =\{v\in V\mid U\perp v\}\le V $ .
-   **Теорема об ортогональном дополнении.** *Пусть $ K $ — поле с инволюцией, $ V $ — вект. простр.-во над $ K $ , $ \sigma\in\overline\rm{SBi}(V)\cup\overline\rm{ABi}(V) $ и $ U,W\le V $ ; тогда
    (1) $ U\subseteq U^{\perp\perp} $ , $ U\subseteq W\,\Rightarrow\,W^\perp \subseteq U^\perp $ , $ (U+W)^\perp =U^\perp \cap W^\perp $ и $ \,U^\perp +W^\perp \subseteq(U\cap W)^\perp $ ;
    (2) если $ \dim V<\infty $ и форма $ \sigma $ невырождена, то $ \dim U^\perp =\dim V-\dim U $ , а также $ U=U^{\perp\perp} $ и $ \,U^\perp +W^\perp =(U\cap W)^\perp $ ;
    (3) $ \rm{Ker}\bigl(\flat\_{\sigma\|\_{U\times U}} \bigr) =U\cap U^\perp $ и, если $ \dim U<\infty $ , то $ \bigl( $ форма $ \sigma\|\_{U\times U} $ невырождена $ \bigr) $ $ \;\Leftrightarrow\;\, $ $ U\cap U^\perp =\{0\} $ ;
    (4) если форма $ \sigma\|\_{U\times U} $ невырождена, то $ V=U\oplus U^\perp $ (и, значит, определен ортогональный проектор на $ U $ : $ \biggl( \begin{align}\rm{proj}\_U\colon V=U\oplus U^\perp &\to V\\v=u+w&\mapsto u\end{align} \biggr) $ ).*

##### 6.4  Диагонализация ¯-симметричных ¯-билинейных форм

-   Ортогональный базис: $ e\in\rm{OOB}(V,\sigma) $ $ \;\Leftrightarrow\; $ $ \bigl( $ $ \sigma\_{e,e} $ — диагональная матрица $ \bigr) $ . Форма $ \sigma $ в ортогональн. коорд. ( $ e\in\rm{OOB}(V,\sigma) $ ): $ \sigma(v,w)=\sum\_{i=1}^n\sigma\_{i,i}\,v^i\overline{w^i} $ .

-   Ортонормированный базис ( $ K=\mathbb R $ или $ K=\mathbb C $ ): $ e\in\rm{OnOB}(V,\sigma) $ $ \;\Leftrightarrow\; $ $ \bigl( $ $ \sigma\_{e,e} $ — диагональная матрица с $ 1,\ldots,1,-1,\ldots,-1,0,\ldots,0 $ на диагонали $ \bigr) $ .

-   **Лемма о неизотропном векторе.** *Пусть $ K $ — поле с инволюцией, $ \rm{char}\,K\ne2 $ , $ V $ — вект. пр. над $ K $ и $ \sigma\in\overline\rm{SBi}(V) \setminus \{0\} $ ; тогда $ \exists\,v\in V\;\bigl(\sigma(v,v)\ne0\bigr) $ .*

-   Теорема Лагранжа. Матричная формулировка теоремы Лагранжа. Алгоритм приведения квадратичной формы к сумме квадратов с коэффициентами.

    **Теорема Лагранжа.** *Пусть $ K $ — поле с инволюцией, $ \rm{char}\,K\ne2 $ , $ V $ — векторное пространство над $ K $ , $ \dim V<\infty $ и $ \sigma\in\overline\rm{SBi}(V) $ ; тогда
    (1) в пространстве $ V $ существует ортогональный базис (то есть $ \rm{OOB}(V,\sigma)\ne\varnothing $ );
    (2) если $ K=\mathbb R $ или $ K=\mathbb C $ , то в пространстве $ V $ существует ортонормированный базис (то есть $ \rm{OnOB}(V,\sigma)\ne\varnothing $ ).*

    **Матричная формулировка теоремы Лагранжа.** *Пусть $ K $ — поле с инволюцией, $ \rm{char}\,K\ne2 $ , $ n\in\mathbb N\_0 $ и $ s\in\overline\rm S\rm{Mat}(n,K) $ ; тогда
    (1) существует такая матрица $ g\in\rm{GL}(n,K) $ , что $ g^{\scriptscriptstyle\mathsf T} \cdot s\cdot\overline g $ — диагональная матрица;
    (2) если $ K=\mathbb R $ или $ K=\mathbb C $ , то сущ.-т такая матрица $ g\in\rm{GL}(n,K) $ , что $ g^{\scriptscriptstyle\mathsf T} \cdot s\cdot\overline g $ — диаг. матрица с $ 1,\ldots,1,-1,\ldots,-1,0,\ldots,0 $ на диагонали.*

-   **Лемма об ортогональном проекторе.** *Пусть $ K $ — поле с инволюцией, $ V $ — вект. пр.-во над $ K $ , $ \sigma\in\overline\rm{SBi}(V) $ , $ U\le V $ , $ m=\dim U<\infty $ , $ e\in\rm{OB}(U) $ ,
    форма $ \sigma\|\_{U\times U} $ невырождена и $ v\in V $ ; тогда $ \rm{proj}\_U(v)^e=(\sigma\|\_{U\times U})^{e,e} \cdot \biggl(\begin{smallmatrix}\sigma(v,e\_1)\\\vdots\\\sigma(v,e\_m)\end{smallmatrix}\biggr) $ и, если $ e\in\rm{OOB}(U,\sigma\|\_{U\times U}) $ , то $ \rm{proj}\_U(v)=\sum\_{i=1}^m\frac{\sigma(v,e\_i)}{\sigma(e\_i,e\_i)}\,e\_i $* .

-   **Лемма об определителе матрицы Грама.** *Пусть $ K $ — поле с инволюцией, $ V $ — векторное простр.-во над $ K $ , $ \sigma\in\overline\rm{SBi}(V) $ , $ m\in\mathbb N $ , $ v\_1,\ldots,v\_m\in V $ ,
    $ U=\langle v\_1,\ldots,v\_{m-1}\rangle $ , форма $ \sigma\|\_{U\times U} $ невырождена и $ \hat v\_m=v\_m-\rm{proj}\_U(v\_m) $ ; тогда $ \det\sigma\_{(v\_1,\ldots,v\_m),(v\_1,\ldots,v\_m)}=\det\sigma\_{(v\_1,\ldots,v\_{m-1}),(v\_1,\ldots,v\_{m-1})}\cdot\sigma(\hat v\_m,\hat v\_m) $ .*

-   **Процесс ортогонализации Грама--Шмидта.** *Пусть $ K $ — поле с инволюцией, $ V $ — векторное пространство над $ K $ , $ n=\dim V<\infty $ , $ \sigma\in\overline\rm{SBi}(V) $ и
    $ e\in\rm{OB}(V) $ ; для любых $ i\in\{0,\ldots,n\} $ обозначим через $ V\_i $ пространство $ \langle e\_1,\ldots,e\_i\rangle $ и обозначим через $ cm\_i $ $ i $ -й угловой минор матрицы $ \sigma\_{e,e} $ (то
    есть $ cm\_i=\det\sigma\_{(e\_1,\ldots,e\_i),(e\_1,\ldots,e\_i)} $ ). Пусть для любых $ i\in\{1,\ldots,n-1\} $ форма $ \sigma\|\_{V\_i\times V\_i} $ невырождена (это эквивалентно тому, что $ cm\_i\ne0 $ ); для
    любых $ i\in\{1,\ldots,n\} $ обозначим через $ \hat e\_i $ вектор $ e\_i-\rm{proj}\_{V\_{i-1}}(e\_i) $ . Тогда для любых $ i\in\{1,\ldots,n\} $ выполнено $ (\hat e\_1,\dots,\hat e\_i)\in\rm{OOB}(V\_i,\sigma\|\_{V\_i\times V\_i}) $ и
    $ \sigma(\hat e\_i,\hat e\_i)=\frac{cm\_i}{cm\_{i-1}} $ , а также $ \hat e\_i=e\_i-\sum\_{j=1}^{i-1}\frac{\sigma(e\_i,\hat e\_j)}{\sigma(\hat e\_j,\hat e\_j)}\,\hat e\_j $ (это индуктивная формула для нахождения векторов $ \hat e\_1,\ldots,\hat e\_n $ ).*

-   Ортогонал. системы функций: $ \cos(nx) $ и $ \sin(nx) $ ( $ n\in\mathbb N $ ), $ \rm e^{nx\,\rm i} $ ( $ n\in\mathbb Z $ ), многочлены Лежандра, Чебышёва, Эрмита (см. пункты 5--10 в § 4 части 2 в [5]).

### 7   Геометрия в векторных пространствах над $ \mathbb R $ или $ \mathbb C $

##### 7.1  Положительно и отрицательно определенные формы и сигнатура формы

-   Мн.-ва положительно и отрицательно определенных форм: $ \overline\rm{SBi}\_{>0}(V)=\{\sigma\in\overline\rm{SBi}(V)\mid\forall\,v\in V \setminus \{0\}\;\bigl(\sigma(v,v)>0\bigr)\} $ и $ \overline\rm{SBi}\_{<0}(V)=-\overline\rm{SBi}\_{>0}(V) $ .
-   Мн.-ва полож. и отриц. опред. матриц: $ \overline\rm S\rm{Mat}\_{>0}(n,K)=\{s\in\overline\rm S\rm{Mat}(n,K)\mid\forall\,v\in K^n \setminus \{0\}\;\bigl(v^{\scriptscriptstyle\mathsf T} \cdot s\cdot\overline v>0\bigr)\} $ и $ \overline\rm S\rm{Mat}\_{<0}(n,K)=-\overline\rm S\rm{Mat}\_{>0}(n,K){} $ .
-   **Следствия из теоремы об ортогональном дополнении и теоремы Лагранжа.** *Пусть $ K=\mathbb R $ или $ K=\mathbb C $ , $ V $ — вект. пр.-во над $ K $ и $ \sigma\in\overline\rm{Bi}(V) $ ; тогда
    (1) если $ \sigma\in\overline\rm{SBi}\_{>0}(V) $ и $ U\le V $ , то $ U\cap U^\perp =\{0\} $ и, если $ \dim U<\infty $ , то форма $ \sigma\|\_{U\times U} $ невырождена и $ V=U\oplus U^\perp $ ;
    (2) если $ n=\dim V<\infty $ , то $ \sigma\in\overline\rm{SBi}\_{>0}(V) $ , если и только если $ \exists\,e\in\rm{OB}(V)\;\bigl(\sigma\_{e,e}=\rm{id}\_n\bigr) $ ;
    (3) если $ n=\dim V<\infty $ и $ e\in\rm{OB}(V) $ , то $ \sigma\in\overline\rm{SBi}\_{>0}(V) $ , если и только если $ \exists\,g\in\rm{GL}(n,K)\;\bigl(\sigma\_{e,e}=g^{\scriptscriptstyle\mathsf T} \cdot\overline g\bigr) $ .*
-   **Критерий Сильвестра.** *Пусть $ K=\mathbb R $ или $ K=\mathbb C $ , $ V $ — векторное пространство над $ K $ , $ n=\dim V<\infty $ , $ \sigma\in\overline\rm{SBi}(V) $ и $ e\in\rm{OB}(V) $ ; для любых
    $ i\in\{1,\ldots,n\} $ обозначим через $ cm\_i $ $ i $ -й угловой минор матрицы $ \sigma\_{e,e} $ (то есть $ cm\_i=\det\sigma\_{(e\_1,\ldots,e\_i),(e\_1,\ldots,e\_i)} $ ); тогда
    (1) $ \sigma\in\overline\rm{SBi}\_{>0}(V) $ , если и только если $ \forall\,i\in\{1,\ldots,n\}\;\bigl(cm\_i>0\bigr) $ ;
    (2) $ \sigma\in\overline\rm{SBi}\_{<0}(V) $ , если и только если $ \forall\,i\in\{1,\ldots,n\}\;\bigl((-1)^i\,cm\_i>0\bigr) $ .*
-   Индексы инерции формы $ \sigma $ : $ \rm{ind}\_{>0}(\sigma)=\max\{\dim U\mid U\le V\,\land\,\sigma\|\_{U\times U} \in\overline{\rm{SBi}}\_{>0}(U)\} $ и $ \rm{ind}\_{<0}(\sigma)=\max\{\dim U\mid U\le V\,\land\,\sigma\|\_{U\times U} \in\overline{\rm{SBi}}\_{<0}(U)\} $ .
-   **Закон инерции Сильвестра.** *Пусть $ K=\mathbb R $ или $ K=\mathbb C $ , $ V $ — векторное простр.-во над $ K $ , $ n=\dim V<\infty $ , $ \sigma\in\overline\rm{SBi}(V) $ и $ e\in\rm{OOB}(V,\sigma) $ ; тогда
    (1) $ \rm{ind}\_{>0}(\sigma)=\|\{i\in\{1,\ldots,n\}\mid\sigma(e\_i,e\_i)>0\}\| $ (и, значит, число $ \|\{i\in\{1,\ldots,n\}\mid\sigma(e\_i,e\_i)>0\}\| $ не зависит от $ e $ );
    (2) $ \rm{ind}\_{<0}(\sigma)=\|\{i\in\{1,\ldots,n\}\mid\sigma(e\_i,e\_i)<0\}\| $ (и, значит, число $ \|\{i\in\{1,\ldots,n\}\mid\sigma(e\_i,e\_i)<0\}\| $ не зависит от $ e $ );
    (3) $ \rm{ind}\_{>0}(\sigma)+\rm{ind}\_{<0}(\sigma)=\rm{rk}(\sigma) $ .*
-   **Теорема о классификации пространств с формой.** *Пусть $ K=\mathbb R $ или $ K=\mathbb C $ , $ V,Y $ — вект. простр.-ва над $ K $ , $ \dim V,\dim Y<\infty $ , $ \sigma\in\overline\rm{SBi}(V) $ и
    $ \varphi\in\overline\rm{SBi}(Y) $ ; тогда $ (V,\sigma)\cong(Y,\varphi) $ , если и только если $ \dim V=\dim Y $ , $ \rm{ind}\_{>0}(\sigma)=\rm{ind}\_{>0}(\varphi) $ и $ \rm{ind}\_{<0}(\sigma)=\rm{ind}\_{<0}(\varphi) $ .*
-   Сигнатура формы $ \sigma $ : $ (\rm{ind}\_{>0}(\sigma),\rm{ind}\_{<0}(\sigma)) $ (или $ \rm{ind}\_{>0}(\sigma)-\rm{ind}\_{<0}(\sigma) $ ). Исследование кривых и поверхностей второго порядка (см. § 2 главы VIII в [1]).

##### 7.2  Предгильбертовы пространства

-   Предгильбертово пространство — вект. пр.-во над $ \mathbb R $ или $ \mathbb C $ с полож. опред. формой. Обозн.-е формы: $ (\,\mid\,) $ . Примеры: $ (v \mid w)=v^{\scriptscriptstyle\mathsf T} \cdot\overline w $ , $ (f \mid g)= \int\_\alpha^\beta  f\,\overline g $ .

-   Евклидово $ \,/\, $ унитарное пр.-во — конечномерн. вект. пр.-во над $ \mathbb R $ $ \,/\, $ $ \mathbb C $ с полож. опред. формой, то есть конечномерн. предгильбертово пр.-во над $ \mathbb R $ $ \,/\, $ $ \mathbb C $ .

-   Норма: $ \\|v\\|=\sqrt{(v \mid v)} $ . Утверждение: *$ v\ne0\,\Rightarrow\,\\|v\\|>0 $ и $ \\|c\,v\\|=\|c\|\,\\|v\\| $* . Гильбертово пространство — полное предгильбертово пр.-во. Пример: $ \ell^2 $ .

-   **Теорема о свойствах нормы.** *Пусть $ V $ — предгильбертово пространство; тогда
    (1) для любых $ v,w\in V $ выполнено $ \|(v \mid w)\|\le\\|v\\|\,\\|w\\| $ (это неравенство Коши--Буняковского--Шварца);
    (2) для любых $ v,w\in V $ выполнено $ \\|v+w\\|\le\\|v\\|+\\|w\\| $ (это неравенство треугольника);
    (3) если $ \dim V<\infty $ , то для любых $ e\in\rm{OnOB}(V) $ и $ v\in V $ выполнено $ v= \sum\_{i=1}^{\dim V} (v \mid e\_i)\,e\_i $ и $ \\|v\\|^2= \sum\_{i=1}^{\dim V} \|(v \mid e\_i)\|^2 $ (это равенство Парсеваля).*

-   Метрика: $ \rm{dist}(v,w)=\\|v-w\\| $ . Расстояние между подмн.-вами: $ \rm{dist}(X,Y)=\inf\,\{\rm{dist}(x,y)\mid x\in X,\,y\in Y\} $ . Теорема о расстояниях и проекциях.

    **Теорема о расстояниях и проекциях.** *Пусть $ V $ — предгильбертово пространство и $ U,U\' \le V $ ; тогда
    (1) для любых $ v,v\' \in V $ выполнено $ \rm{dist}(v+U,v\'+U\')=\rm{dist}(v-v\',U+U\') $ ;
    (2) если $ \dim U<\infty $ , то для любых $ v\in V $ выполнено $ \rm{dist}(v,U)=\rm{dist}(v,\rm{proj}\_U(v)) $ ;
    (3) если $ \dim V<\infty $ , то $ \rm{proj}\_U +\rm{proj}\_{U^\perp} =\rm{id}\_V $ и для любых $ v\in V $ выполнено $ \rm{dist}(v,U)=\\|\rm{proj}\_{U^\perp} (v)\\| $ ;
    (4) если $ \dim U<\infty $ , то для любых $ e\in\rm{OnOB}(U) $ и $ v\in V $ выполнено $ \rm{proj}\_U(v)= \sum\_{i=1}^{\dim U} (v \mid e\_i)\,e\_i $ и $ \\|v\\|^2\ge \sum\_{i=1}^{\dim U} \|(v \mid e\_i)\|^2 $ (это неравенство Бесселя).*

-   Метод наименьших квадратов: замена системы $ a\cdot v=y $ , где $ a\in\rm{Mat}(p,n,\mathbb R) $ и $ \rm{rk}(a)=n $ , на систему $ a\cdot v=\rm{proj}\_X(y) $ , где $ X=\{a\cdot v\mid v\in\mathbb R^n\} $ .

-   Угол между векторами и между вектором и подпр.-вом ( $ K=\mathbb R $ , $ v\ne0 $ , $ w\ne0 $ , $ U\ne\{0\} $ ): $ \angle(v,w)=\arccos\frac{(v \mid w)}{\\|v\\|\,\\|w\\|}{} $ и $ \angle(v,U)=\arccos\frac{\\|\rm{proj}\_U(v)\\|}{\\|v\\|} $ .

-   Псевдоевклидово $ \,/\, $ псевдоунитарное пр.-во сигнатуры $ (p,q) $ — кон.-мерн. вект. пр.-во над $ \mathbb R $ $ \,/\, $ $ \mathbb C $ с невыр. ¯-симметр. ¯-билин. формой сигнатуры $ (p,q) $ .

##### 7.3  Ориентация, объем, векторное произведение

-   Отн.-е одинак. ориентированности ( $ V $ — кон.-мерн. в. пр. над $ \mathbb R $ , $ e,\tilde e\in\rm{OB}(V) $ ): $ e\overset{\scriptscriptstyle\rm{or}}\sim\tilde e\,\Leftrightarrow\,\det\rm c\_e^\tilde e >0 $ . Утверждение: $ V\ne\{0\}\,\Rightarrow\,\|\rm{OB}(V)/{\overset{\scriptscriptstyle\rm{or}}\sim}\|=2 $ .

-   Ориентация пр.-ва $ V $ — выбор эл.-та $ \rm{OB}\_{>0}(V) $ мн.-ва $ \rm{OB}(V)/\overset{\scriptscriptstyle\rm{or}}\sim $ . Знак набора векторов: $ \rm{sign}(v\_1,\ldots,v\_n) $ . Теорема о знаке базиса и формах объема.

    **Теорема о знаке базиса и формах объема.** *Пусть $ V $ — векторное простр.-во с ориентацией и $ e\in\rm{OB}(V) $ ; тогда для любых $ \tilde e\in\rm{OB}(V) $ выполнено
    $ \rm{sign}(\tilde e)\,\rm{vol}^\tilde e =\|\det\rm c\_e^\tilde e\|\,\rm{sign}(e)\,\rm{vol}^e $ , а также множество $ \rm{VF}\_{>0}(V) $ , равное $ \,\mathbb R\_{>0}\,\rm{sign}(e)\,\rm{vol}^e $ , не зависит от выбора упорядоченного базиса $ e $ .*

-   Каноническая форма объема в псевдоевкл. пр.-ве с ориентацией ( $ e\in\rm{OB}(V) $ ): $ \rm{vol}=\rm{sign}(e)\sqrt{\|\det\sigma\_{e,e}\|}\,\rm{vol}^e $ ; если $ e\in\rm{OnOB}\_{>0}(V) $ , то $ \rm{vol}=\rm{vol}^e $ .

-   Корректность опр.-я объема. Объем в коорд.: $ \rm{vol}(v\_1,\ldots,v\_n)=\rm{sign}(e)\sqrt{\|\det\sigma\_{e,e}\|}   \sum\_{1\le j\_1,\ldots,j\_n\le n}   \varepsilon\_{j\_1,\ldots,j\_n}v\_1^{j\_1} \cdot\ldots\cdot v\_n^{j\_n} $ . Лемма об объеме и матрице Грама.

    **Лемма об объеме и матрице Грама.** *Пусть $ V $ — псевдоевклидово пространство сигнатуры $ (p,q) $ с ориентацией, $ n=p+q $ и $ v\_1,\ldots,v\_n\in V $ ; тогда
    (1) $ \rm{vol}(v\_1,\ldots,v\_n)=\rm{sign}(v\_1,\ldots,v\_n)\sqrt{\|\det\sigma\_{(v\_1,\ldots,v\_n),(v\_1,\ldots,v\_n)}\|} $ ;
    (2) для любых $ w\_1,\ldots,w\_n\in V $ выполнено $ \rm{vol}(v\_1,\ldots,v\_n)\cdot\rm{vol}(w\_1,\ldots,w\_n)=(-1)^q\det\sigma\_{(v\_1,\ldots,v\_n),(w\_1,\ldots,w\_n)} $ .*

-   Неотриц. объем в евкл. пр.-ве: $ \|\rm{vol}\|\_m(v\_1,\ldots,v\_m)=\|\rm{vol}(v\_1,\ldots,v\_m)\| $ в $ \langle v\_1,\ldots,v\_m\rangle $ , если $ v\_1,\ldots,v\_m $ независимы; иначе $ \|\rm{vol}\|\_m(v\_1,\ldots,v\_m)=0 $ .

-   **Теорема о неотрицательном объеме в евклидовом пространстве.** *Пусть $ V $ — евклидово пространство, $ m\in\mathbb N\_0 $ и $ v\_1,\ldots,v\_m\in V $ ; тогда
    (1) $ \|\rm{vol}\|\_m(v\_1,\ldots,v\_m)=\sqrt{\det\sigma\_{(v\_1,\ldots,v\_m),(v\_1,\ldots,v\_m)}} $ ;
    (2) если $ m\ge1 $ и $ \hat v\_m=v\_m-\rm{proj}\_{\langle v\_1,\ldots,v\_{m-1}\rangle}(v\_m) $ , то $ \|\rm{vol}\|\_m(v\_1,\ldots,v\_m)=\|\rm{vol}\|\_{m-1}(v\_1,\ldots,v\_{m-1})\cdot\\|\hat v\_m\\| $ .*

-   Вект. произв. в псевдоевкл. пр.-ве с ориент.: $ v\_1\times\ldots\times v\_{n-1}=\sharp\,\bigl(v\_n \mapsto\rm{vol}(v\_1,\ldots,v\_n)\bigr) $ ( $ \Leftrightarrow\,\forall\,v\_n\in V\;\bigl((v\_1\times\ldots\times v\_{n-1} \mid v\_n)=\rm{vol}(v\_1,\ldots,v\_n)\bigr) $ ).

-   Векторное произведение в коорд.: $ (v\_1\times\ldots\times v\_{n-1})^i=\rm{sign}(e)\sqrt{\|\det\sigma\_{e,e}\|}   \sum\_{1\le j\_1,\ldots,j\_n\le n}   \sigma^{i,j\_n}\varepsilon\_{j\_1,\ldots,j\_n}v\_1^{j\_1} \cdot\ldots\cdot v\_{n-1}^{j\_{n-1}} $ . Теорема о векторном произведении.

    **Теорема о векторном произведении.** *Пусть $ V $ — псевдоевклидово пр.-во сигнатуры $ (p,q) $ с ориентацией, $ n=p+q\ge1 $ и $ v\_1,\ldots,v\_{n-1}\in V $ ; тогда
    (1) $ v\_1\times\ldots\times v\_{n-1}\in\langle v\_1,\ldots,v\_{n-1}\rangle^\perp $ , а также $ v\_1\times\ldots\times v\_{n-1}\ne0 $ , если и только если векторы $ v\_1,\ldots,v\_{n-1} $ независимы;
    (2) если $ q=0 $ , то $ \\|v\_1\times\ldots\times v\_{n-1}\\|=\|\rm{vol}\|\_{n-1}(v\_1,\ldots,v\_{n-1}) $ и, если $ v\_1,\ldots,v\_{n-1} $ независимы, то $ (v\_1,\ldots,v\_{n-1},v\_1\times\ldots\times v\_{n-1})\in\rm{OB}\_{>0}(V) $ ;
    (3) для любых $ w\_1,\ldots,w\_{n-1}\in V $ выполнено $ (v\_1\times\ldots\times v\_{n-1} \mid w\_1\times\ldots\times w\_{n-1})=(-1)^q\det\sigma\_{(v\_1,\ldots,v\_{n-1}),(w\_1,\ldots,w\_{n-1})} $ ;
    (4) если $ n=3 $ и $ q=0 $ , то для любых $ u,v,w\in V $ выполнено $ (u\times v)\times w=(u \mid w)\,v-(v \mid w)\,u\, $ и $ \,(u\times v)\times w+(v\times w)\times u+(w\times u)\times v=0 $ .*

##### 7.4  Автоморфизмы пространств с формой, ортогональные и унитарные операторы и матрицы

-   Группа автоморфизмов пр.-ва с ¯-билинейной формой: $ \rm{Aut}(V,\sigma)=\rm{Iso}((V,\sigma),(V,\sigma))=\{a\in\rm{GL}(V)\mid\forall\,v,w\in V\;\bigl(\sigma(a(v),a(w))=\sigma(v,w)\bigr)\} $ .
-   Утверждение: *пусть $ \rm{char}\,K\ne2 $ и $ \sigma\in\rm{SBi}(V) $ , или $ K=\mathbb C $ и $ \sigma\in\overline\rm{Bi}(V) $ ; тогда $ \,\rm{Aut}(V,\sigma)=\{a\in\rm{GL}(V)\mid\forall\,v\in V\;\bigl(\sigma(a(v),a(v))=\sigma(v,v)\bigr)\} $* .
-   Ортогональная группа ( $ V $ — в. пр. над $ \mathbb R $ , $ \sigma\in\rm{SBi}(V) $ ): $ \rm O(V)=\rm{Aut}(V,\sigma) $ . Унитарная группа ( $ V $ — в. пр. над $ \mathbb C $ , $ \sigma\in\overline\rm{SBi}(V) $ ): $ \rm U(V)=\rm{Aut}(V,\sigma) $ .
-   **Лемма об автоморфизмах пространств с формой и матрицах.**
    *(1) Пусть $ K $ — поле с инволюцией, $ V $ — векторное пространство над $ K $ , $ n=\dim V<\infty $ , $ \sigma\in\overline\rm{Bi}(V) $ , $ a\in\rm{End}(V) $ и $ e\in\rm{OB}(V) $ ; тогда
    $ a\in\rm{Aut}(V,\sigma)\,\Leftrightarrow\,a\_e^e\in\rm{GL}(n,K)\,\land\,(a\_e^e)^{\scriptscriptstyle\mathsf T} \cdot\sigma\_{e,e} \cdot\overline{a\_e^e}=\sigma\_{e,e} $ и, если форма $ \sigma $ невырождена, то условие « $ \,a\_e^e\in\rm{GL}(n,K) $ » можно убрать.
    (2) Пусть $ V $ — псевдоевклидово пространство сигнатуры $ (p,q) $ и $ e,\tilde e\in\rm{OnOB}(V) $ ; тогда $ (\rm c\_\tilde e^e)^{\scriptscriptstyle\mathsf T} \cdot \Bigl(\begin{smallmatrix}\rm{id}\_p&0\\0&-\rm{id}\_q\end{smallmatrix}\Bigr) \cdot\rm c\_\tilde e^e= \Bigl(\begin{smallmatrix}\rm{id}\_p&0\\0&-\rm{id}\_q\end{smallmatrix}\Bigr) $ .
    (3) Пусть $ V $ — псевдоунитарное пространство сигнатуры $ (p,q) $ и $ e,\tilde e\in\rm{OnOB}(V) $ ; тогда $ (\rm c\_\tilde e^e)^{\scriptscriptstyle\mathsf T} \cdot \Bigl(\begin{smallmatrix}\rm{id}\_p&0\\0&-\rm{id}\_q\end{smallmatrix}\Bigr) \cdot\overline{\rm c\_\tilde e^e}= \Bigl(\begin{smallmatrix}\rm{id}\_p&0\\0&-\rm{id}\_q\end{smallmatrix}\Bigr) $ .*
-   Матричные ортогонал. группы: $ \rm O(p,q)=\{a\in\rm{Mat}(p+q,\mathbb R)\mid a^{\scriptscriptstyle\mathsf T} \cdot \Bigl(\begin{smallmatrix}\rm{id}\_p&0\\0&-\rm{id}\_q\end{smallmatrix}\Bigr) \cdot a= \Bigl(\begin{smallmatrix}\rm{id}\_p&0\\0&-\rm{id}\_q\end{smallmatrix}\Bigr)\} $ , $ \rm{SO}(p,q)=\rm{SL}(p+q,\mathbb R)\cap\rm O(p,q) $ и $ \rm O(n) $ , $ \rm{SO}(n) $ .
-   Матричные унитарные группы: $ \rm U(p,q)=\{a\in\rm{Mat}(p+q,\mathbb C)\mid a^{\scriptscriptstyle\mathsf T} \cdot \Bigl(\begin{smallmatrix}\rm{id}\_p&0\\0&-\rm{id}\_q\end{smallmatrix}\Bigr) \cdot\overline a= \Bigl(\begin{smallmatrix}\rm{id}\_p&0\\0&-\rm{id}\_q\end{smallmatrix}\Bigr)\} $ , $ \rm{SU}(p,q)=\rm{SL}(p+q,\mathbb C)\cap\rm U(p,q) $ и $ \rm U(n) $ , $ \rm{SU}(n) $ .
-   Примеры: $ \rm{SO}(2)=\bigl\{\Bigl(\begin{smallmatrix}\cos\varphi&-{\sin\varphi}\\\sin\varphi&\cos\varphi\end{smallmatrix}\Bigr) \mid\varphi\in[0;2\pi)\bigr\} $ , $ \rm O(2)=\rm{SO}(2)\cup\bigl\{\Bigl(\begin{smallmatrix}\cos\varphi&\sin\varphi\\\sin\varphi&-{\cos\varphi}\end{smallmatrix}\Bigr) \mid\varphi\in[0;2\pi)\bigr\} $ и $ \rm{SU}(2)=\bigl\{\Bigl(\begin{smallmatrix}c&d\\-\overline d&\overline c\end{smallmatrix}\Bigr) \mid c,d\in\mathbb C,\,\|c\|^2 +\|d\|^2 =1\bigr\} $ .
-   **Теорема Эйлера о вращениях.** *Пусть $ V $ — евклидово пр.-во с ориентацией, $ \dim V=3 $ и $ a\in\rm{SO}(V) $ ; тогда существуют такие $ e\in\rm{OnOB}\_{>0}(V) $ и
    $ \varphi\in[0;2\pi) $ , что $ a\_e^e=\biggl(\begin{smallmatrix}1&0&0\\0&\cos\varphi&-{\sin\varphi}\\0&\sin\varphi&\cos\varphi\end{smallmatrix}\biggr) $ (и, значит, $ a $ — оператор поворота в $ V $ на угол $ \varphi $ против часовой стрелки вокруг оси с напр. вектором $ e\_1 $ ).*
-   Группа изометрий предгильбертова пр.-ва (как метрического пространства): $ \rm{Isom}(V)=\{a\in\rm{Bij}(V)\mid\forall\,v,w\in V\;\bigl(\rm{dist}(a(v),a(w))=\rm{dist}(v,w)\bigr)\} $ .
-   **Теорема об описании изометрий.** *Пусть $ V $ — предгильбертово пространство над $ \,\mathbb R $ ; тогда $ \{a\in\rm{Isom}(V)\mid a(0)=0\}=\rm O(V) $ , а также, обозначая
    через $ G $ , $ F $ и $ H $ группу $ \,\rm{Isom}(V) $ и ее подгруппы $ \{\bigl(v\mapsto v+z\bigr) \mid z\in V\} $ и $ \{a\in\rm{Isom}(V)\mid a(0)=0\} $ соответственно, имеем следующие факты:
    $ F\cap H=\{\rm{id}\_V\} $ , $ G=F\circ H $ , $ \forall\,h\in H\;\bigl(h\circ F\circ h^{-1} \subseteq F\bigr) $ и $ F\cong V^+  $ (и, значит, $ \rm{Isom}(V)=\{\bigl(v\mapsto a(v)+z\bigr) \mid a\in\rm O(V),\,z\in V\}\cong V^+ \leftthreetimes\rm O(V) $ ).*

##### 7.5  Тело кватернионов

-   Кольцо кватернионов: $ \mathbb H=\{\alpha+\beta\,\rm i+\gamma\,\rm j+\delta\,\rm k\mid\alpha,\beta,\gamma,\delta\in\mathbb R\} $ , где $ \rm i^2=\rm j^2=\rm k^2=-1 $ , а также $ \rm i\,\rm j=-\rm j\,\rm i=\rm k $ , $ \rm j\,\rm k=-\rm k\,\rm j=\rm i $ и $ \rm k\,\rm i=-\rm i\,\rm k=\rm j $ .

-   Скалярная (вещественная) часть и векторная (мнимая) часть кватерниона: $ \rm{Re}(\alpha+\beta\,\rm i+\gamma\,\rm j+\delta\,\rm k)=\alpha $ и $ \rm{Im}(\alpha+\beta\,\rm i+\gamma\,\rm j+\delta\,\rm k)=\beta\,\rm i+\gamma\,\rm j+\delta\,\rm k $ .

-   Пр.-во чистых кватернионов: $ \mathbb H\_\rm{vect} =\{v\in\mathbb H\mid\rm{Re}(v)=0\} $ . Скалярное произв.-е, векторное произв.-е, норма в $ \mathbb H\_\rm{vect} $ : $ (v \mid w) $ , $ v\times w $ , $ \\|v\\|=\sqrt{(v \mid v)} $ .

-   Утверждение: $ \forall\,v,w\in\mathbb H\_\rm{vect}\,\bigl(v\,w=-(v \mid w)+v\times w\;\land\;v^2=-\\|v\\|^2\bigr) $ . Сопряжение: $ \overline a=\rm{Re}(a)-\rm{Im}(a) $ . Модуль: $ \|a\|=\sqrt{\rm{Re}(a)^2+\\|\rm{Im}(a)\\|^2} $ .

-   **Теорема о свойствах кватернионов.**
    *(1) Для любых $ a\in\mathbb H $ выполнено $ a\,\overline a=\overline a\,a=\|a\|^2 $ и, если $ a\ne0 $ , то $ a^{-1} = \frac{\overline a}{\|a\|^2} $ (и, значит, $ \mathbb H $ — тело).
    (2) Для любых $ a,b\in\mathbb H $ выполнено $ \overline{a+b}=\overline a+\overline b $ и $ \overline{a\,b}=\overline b\,\overline a $ (и, значит, отображение $ \biggl( \begin{align}\mathbb H&\to\mathbb H\\a&\mapsto\overline a\end{align} \biggr) $ — антиавтоморфизм тела $ \,\mathbb H $ ).
    (3) Для любых $ a,b\in\mathbb H $ выполнено $ \|a\,b\|=\|a\|\,\|b\| $ (и, значит, отображение $ \biggl( \begin{align}\mathbb H^\times  &\to\mathbb R\_{>0} \\a&\mapsto\|a\|\end{align} \biggr) $ — гомоморфизм групп).*

-   Группа $ \rm S^3 $ : $ \rm S^3 =\{g\in\mathbb H\mid\|g\|=1\} $ . Утверждение: $ \mathbb H^\times \cong\mathbb R\_{>0} \times\rm S^3 $ . Экспонента от кватерниона $ a $ : $ \rm e^a =\sum\_{k=0}^\infty\frac1{k!}\,a^k $ . Теорема о свойствах экспоненты.

    **Теорема о свойствах экспоненты.**
    *(1) Для любых $ a,b\in\mathbb H $ выполнено $ a\,b=b\,a\,\Rightarrow\,\rm e^{a+b} =\rm e^a \cdot\rm e^b $ , а также $ \rm e^0 =1 $ и $ \rm e^{-a} =(\rm e^a)^{-1} $ .
    (2) Для любых $ \varphi\in\mathbb R $ и таких $ u\in\mathbb H\_\rm{vect} $ , что $ \\|u\\|=1 $ , выполнено $ \rm e^{\varphi\,u} =\cos\varphi+\sin\varphi\;u $ (и, значит, $ \rm S^3 =\{\rm e^{\varphi\,u} \mid\varphi\in[0;\pi],\,u\in\mathbb H\_\rm{vect},\,\\|u\\|=1\} $ ).*

-   **Теорема об описании поворотов при помощи кватернионов.** *(1) Пусть $ \varphi\in\mathbb R $ , $ u\in\mathbb H\_\rm{vect} $ и $ \\|u\\|=1 $ ; тогда $ \biggl( \begin{align}\mathbb H\_\rm{vect} &\to\mathbb H\_\rm{vect}\\v&\mapsto\rm e^{\varphi\,u}\,v\,\rm e^{-\varphi\,u} \end{align} \biggr) $ — оператор
    поворота в пространстве $ \,\mathbb H\_\rm{vect} $ на угол $ 2\varphi $ против часовой стрелки вокруг оси с направляющим вектором $ u $ .
    (2) Отображение $ \biggl( \begin{align}\rm S^3 /\{1,-1\}&\to\rm{SO}(\mathbb H\_\rm{vect})\\\{g,-g\}&\mapsto\bigl(v\mapsto g\,v\,g^{-1}\bigr) \end{align} \biggr) $ определено корректно и является изоморфизмом групп (и, значит, $ \rm S^3 /\{1,-1\}\cong\rm{SO}(3) $ ).*

### 8   Алгебры

##### 8.1  Определения и конструкции, связанные с алгебрами

-   $ K $ -Алгебра — вект. пространство над $ K $ с билинейным умножением — кольцо в широком смысле слова с «правильным» умножением на скаляры из $ K $ .

-   Примеры: $ \rm{Func}(X,K) $ , $ K[x] $ , $ K(x) $ , $ \rm{Mat}(n,K) $ , $ \rm{End}(V) $ ; $ \mathbb R $ -алгебры $ \mathbb C $ , $ \mathbb H $ , $ \rm C^0 (X,\mathbb R) $ , $ \rm C^\infty (M,\mathbb R) $ . Структурн. константы алгебры: $ m^i\_{j\_1,j\_2}  =(e\_{j\_1}e\_{j\_2})^i $ .

-   Теорема Кэли для ассоциативных алгебр с $ 1 $ . Инъект. гомоморфизмы $ \mathbb R $ -алгебр: $ \biggl( \begin{align}\mathbb C&\to\rm{Mat}(2,\mathbb R)\,\\\alpha+\beta\,\rm i&\mapsto \Bigl(\begin{smallmatrix}\alpha&-\beta\\\beta&\alpha\end{smallmatrix}\Bigr)\end{align} \biggr) $ и $ \biggl( \begin{align}\mathbb H&\to\rm{Mat}(2,\mathbb C)\\\alpha+\beta\,\rm i+\gamma\,\rm j+\delta\,\rm k&\mapsto \Bigl(\begin{smallmatrix}\alpha+\beta\,\rm i&\gamma+\delta\,\rm i\\-\gamma+\delta\,\rm i&\alpha-\beta\,\rm i\end{smallmatrix}\Bigr)\end{align} \biggr) $ .

    **Теорема Кэли для ассоциативных алгебр с 1.** *Пусть $ K $ — поле и $ A $ — ассоциативная $ K $ -алгебра с $ 1 $ ; обозначим через $ {}\_K A $ векторное пространство
    над $ K $ , получающееся из $ A $ при «забывании» умножения в этой алгебре, и для любых $ a\in A $ обозначим через $ \rm{lm}\_a $ отображение $ \biggl( \begin{align}A&\to A\\b&\mapsto a\,b\end{align} \biggr) $ ; тогда
    отобр. $ \biggl( \begin{align}A&\to\rm{End}({}\_K A)\\a&\mapsto\rm{lm}\_a\end{align} \biggr) $ определено корректно и является инъективным гомоморфизмом алгебр с $ 1 $ (и, значит, $ A\cong\{\rm{lm}\_a \mid a\in A\}\le\rm{End}({}\_K A) $ ).*

-   Алгебра с делением: $ \forall\,a\in A \setminus \{0\}\;\bigl(\rm{lm}\_a,\rm{rm}\_a \in\rm{Bij}(A)\bigr) $ и $ A\ne\{0\} $ . Примеры: $ K $ , $ K(x) $ ; $ \mathbb R $ -алгебры с делением $ \mathbb C $ , $ \mathbb H $ , алгебра октонионов (октав) $ \mathbb O $ .

-   Моноидная алгебра ( $ M $ — моноид): $ K[M]=\rm{FinFunc}(M,K) $ ; общий вид эл.-та: $ \sum\_{m\in M}p\_mm $ ( $ \|\{m\in M\mid p\_m\ne0\}\|<\infty $ ); умнож.-е в $ K[M] $ : свертка.

-   Алгебра многочленов от свободных (некоммутирующих) перем.: $ K\langle x\_1,\ldots,x\_n\rangle=K[\rm W(x\_1,\ldots,x\_n)] $ . Степень многочлена. Однородные многочлены.

-   Алгебра многочленов от коммутирующих переменных: $ K[x\_1,\ldots,x\_n]=K[\rm W(x\_1,\ldots,x\_n)^\mathsf{ab}]\cong K\langle x\_1,\ldots,x\_n\rangle/\bigl(\{x\_ix\_j-x\_jx\_i \mid i,j\in\{1,\ldots,n\}\}\bigr) $ .

-   Алгебра многочленов от антикоммут. (грассмановых) перем.: $ K\_\wedge[x\_1,\ldots,x\_n]=K\langle x\_1,\ldots,x\_n\rangle/\bigl(\{x\_ix\_j+x\_jx\_i \mid i,j\in\{1,\ldots,n\}\}\cup\{x\_1^2,\ldots,x\_n^2\}\bigr) $ .

##### 8.2  Алгебры Ли (основные определения и примеры)

-   $ K $ -Алгебра Ли — $ K $ -алгебра, умножение в которой антисимметрично ( $ [a,a]=0 $ ) и удовлетв.-т тождеству Якоби ( $ [[a,b],c]+[[b,c],a]+[[c,a],b]=0 $ ).

-   Коммутатор эл.-тов ассоциативной алгебры: $ [a,b]=a\,b-b\,a $ . Алгебра $ A^{(-)} $ : вект. простр.-во $ {}\_K A $ с операцией $ [\,,] $ . Утверждение: *$ A^{(-)} $ — алгебра Ли*.

-   Примеры: $ \mathfrak{gl}(V)=\rm{End}(V)^{(-)} $ , $ \mathfrak{sl}(V)=\{a\in\mathfrak{gl}(V)\mid\rm{tr}\,a=0\} $ , трехмерное евклид. пр.-во с ориент. относ.-но $ \times $ , $ \mathbb H\_\rm{vect} $ — подалгебра алгебры $ \mathbb H^{(-)} $ .

-   Матричные алгебры Ли: $ \mathfrak{gl}(n,K) $ , $ \mathfrak{sl}(n,K) $ , $ \mathfrak o(n)=\mathfrak{so}(n)=\{a\in\mathfrak{gl}(n,\mathbb R)\mid a^{\scriptscriptstyle\mathsf T} =-a\} $ , $ \mathfrak u(n)=\{a\in\mathfrak{gl}(n,\mathbb C)\mid a^{\scriptscriptstyle\mathsf T} =-\overline a\} $ , $ \mathfrak{su}(n)=\mathfrak{sl}(n,\mathbb C)\cap\mathfrak u(n){} $ .

-   **Теорема о группах матриц и матричных алгебрах Ли.** *Пусть $ K=\mathbb R $ или $ K=\mathbb C $ и $ n\in\mathbb N\_0 $ ; для любых $ G\le\rm{GL}(n,K) $ обозначим через $ \,\rm T\_{\rm{id}\_n}G $ мн.-во
    $ \{\dot\gamma(0)\mid\alpha\in[-\infty;0),\,\beta\in(0;\infty],\,\gamma\in\rm C^\infty ((\alpha;\beta),\rm{Mat}(n,K)),\,\rm{Im}\,\gamma\subseteq G,\,\gamma(0)=\rm{id}\_n\} $ (это касательное пр.-во к группе $ G $ в точке $ \,\rm{id}\_n $ ); тогда
    $ \rm T\_{\rm{id}\_n}\rm{GL}(n,K)=\mathfrak{gl}(n,K) $ и $ \,\rm T\_{\rm{id}\_n}\rm{SL}(n,K)=\mathfrak{sl}(n,K) $ , а также $ \,\rm T\_{\rm{id}\_n}\rm O(n)=\rm T\_{\rm{id}\_n}\rm{SO}(n)=\mathfrak{so}(n) $ , $ \rm T\_{\rm{id}\_n}\rm U(n)=\mathfrak u(n) $ и $ \,\rm T\_{\rm{id}\_n}\rm{SU}(n)=\mathfrak{su}(n) $ .*

-   Теорема Кэли для алгебр Ли. Изоморфизмы $ \mathbb R $ -алгебр Ли: $ \Biggl( \begin{align}\mathbb R^3 &\to\mathfrak{so}(3)\\\biggl(\begin{smallmatrix}\beta\\\gamma\\\delta\end{smallmatrix}\biggr) &\mapsto \biggl(\begin{smallmatrix}0&-\delta&\gamma\\\delta&0&-\beta\\-\gamma&\beta&0\end{smallmatrix}\biggr)\end{align} \Biggr) $ , $ \Biggl( \begin{align}\mathbb R^3 &\to\mathbb H\_\rm{vect}\\\biggl(\begin{smallmatrix}\beta\\\gamma\\\delta\end{smallmatrix}\biggr) &\mapsto{\textstyle\frac12}(\beta\,\rm i+\gamma\,\rm j+\delta\,\rm k)\end{align} \Biggr) $ и $ \Biggl( \begin{align}\mathbb R^3 &\to\mathfrak{su}(2)\\\biggl(\begin{smallmatrix}\beta\\\gamma\\\delta\end{smallmatrix}\biggr) &\mapsto{\textstyle\frac12}\Bigl(\begin{smallmatrix}\beta\,\rm i&\gamma+\delta\,\rm i\\-\gamma+\delta\,\rm i&-\beta\,\rm i\end{smallmatrix}\Bigr)\end{align} \Biggr) $ .

    **Теорема Кэли для алгебр Ли.** *Пусть $ K $ — поле и $ \mathfrak g $ — $ K $ -алгебра Ли; обозначим через $ {}\_K\mathfrak g $ векторное пространство над $ K $ , получающееся из $ \mathfrak g $ при
    «забывании» умножения в этой алгебре, и для любых $ a\in\mathfrak g $ обозначим через $ \rm{ad}\_a $ отображение $ \biggl( \begin{align}\mathfrak g&\to\mathfrak g\\b&\mapsto[a,b]\end{align} \biggr) $ ; тогда отображение $ \biggl( \begin{align}\mathfrak g&\to\mathfrak{gl}({}\_K\mathfrak g)\\a&\mapsto\rm{ad}\_a\end{align} \biggr) $
    определено корректно и является гомоморфизмом алгебр Ли.*

-   Алгебра Ли дифференцирований $ K $ -алгебры $ A $ : $ \rm{Der}(A)=\{d\in\mathfrak{gl}({}\_K A)\mid\forall\,a,b\in A\;\bigl(d(a\,b)=d(a)\,b+a\,d(b)\bigr)\} $ — подалгебра алгебры $ \mathfrak{gl}({}\_K A) $ .

-   Дифференциров.-е (производная Ли) по вект. полю ( $ M $ — откр. мн.-во в $ \mathbb R^n $ , $ A=\rm C^\infty (M,\mathbb R) $ , $ v\in\rm C^\infty (M,\mathbb R^n) $ ): $ \biggl(\begin{align}\mathcal L\_v\colon A&\to A\\f&\mapsto\textstyle\sum\_{i=1}^nv^i\frac{\partial f}{\partial x^i}\end{align} \biggr) \in\rm{Der}(A) $ .
