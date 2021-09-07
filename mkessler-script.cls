\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{mkessler-script}[2021/03/31 Write up lecture notes as script]

%%%%Options of the package
\newif\ifenglish\englishtrue
\DeclareOption{english}{\englishtrue}
\DeclareOption{german}{\englishfalse}

\newif\ifshowversion\showversiontrue
\DeclareOption{show version}{\showversiontrue}
\DeclareOption{hideversion}{\showversionfalse}

\ProcessOptions\relax


%%%%Define command to set metainformation of document
%Set the course
\def\@course{\ClassError{mkessler-script}{No \noexpand\course given}{See documentation for details}}%
\DeclareRobustCommand*{\course}[1]{\gdef\@course{#1}}

\def\@lecturer{\ClassError{mkessler-script}{No \noexpand\lecturer given}{See documentation for details}}%
\def\@lecturertitle{}
\DeclareRobustCommand*{\lecturer}[2][]{
    \gdef\@lecturer{#2}
    \gdef\@lecturertitle{\ifenglish Lecturer\else\ifthenelse{\isempty{#1}}{Dozent}{Dozentin}\fi}{}
}

%Set the assistant
\newif\ifprintassistant\printassistantfalse
\def\@assistant{}%
\def\@assistantitle{}
\DeclareRobustCommand*{\assistant}[2][]{
    \printassistanttrue
    \gdef\@assistant{#2}
    \gdef\@assistanttitle{\ifenglish Assistant\else\ifthenelse{\isempty{#1}}{Assistent}{Assistentin}\fi}
}

%%%%Load base class article
\LoadClass{article}

%%%%Title
%Define layout of title using course, lecturer, assistant and author, and optionally the current time
\RequirePackage{xparse}
\RequirePackage{datetime}
\renewcommand\@maketitle{%
  \newpage
  \null
  \vskip 2em%
  \begin{center}%
  \let \footnote \thanks
    {\LARGE \@course \par}%
    \vskip 1.5em%
    {\large
      \lineskip .5em%
      \begin{tabular}[t]{c}%
        \@lecturertitle \\
        {\sc \@lecturer} \\
      \end{tabular}\par
    \ifprintassistant
    \vskip 1em%
        \begin{tabular}[t]{c}%
        \@assistanttitle \\
        {\sc \@assistant} \\
        \end{tabular}\par
    \fi
    \vskip 1em%
        \begin{tabular}[t]{c}%
        \ifenglish Notes\else Mitschrift\fi \\
        {\sc \@author} \\
        \end{tabular}
        \par}%
    \ifshowversion
    \vskip 3em%
        \begin{tabular}[t]{c}%
        {\small Version} \\
        \today\,\currenttime
        \end{tabular}\par
    \fi
    \vskip 4em%
  \end{center}%
  \par
  \vskip 1.5em
}


%%%The following is based on the repository
% https://github.com/gillescastel/university-setup
% but has been modified for own purposes. The original content is distributed under the following license:

%MIT License

%Copyright (c) 2019 Gilles Castel

%Permission is hereby granted, free of charge, to any person obtaining a copy
%of this software and associated documentation files (the "Software"), to deal
%in the Software without restriction, including without limitation the rights
%to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
%copies of the Software, and to permit persons to whom the Software is
%furnished to do so, subject to the following conditions:
%
%The above copyright notice and this permission notice shall be included in all
%copies or substantial portions of the Software.
%
%THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
%IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
%FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
%AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
%LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
%OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
%SOFTWARE.

%%%% These are the fancy headers
\RequirePackage{fancyhdr}
\pagestyle{fancy}

% LE: left even
% RO: right odd
% CE, CO: center even, center odd

\fancyhead[RO,LE]{\@lecture} % Right odd,  Left even
\fancyhead[RE,LO]{}          % Right even, Left odd

\fancyfoot[RO,LE]{\thepage}  % Right odd,  Left even
\fancyfoot[RE,LO]{}          % Right even, Left odd
\fancyfoot[C]{\leftmark}     % Center

\makeatother

%%No fancy headers in the appendix (as there is no lecture)
\let\oldappendix\appendix
\renewcommand\appendix{
    \oldappendix
    \fancyhead[RO,LE]{}
    \renewcommand{\headrulewidth}{0pt}
}

% Fix some stuff
% %http://tex.stackexchange.com/questions/76273/multiple-pdfs-with-page-group-included-in-a-single-page-warning
\pdfsuppresswarningpagegroup=1

% Fix some spacing
% http://tex.stackexchange.com/questions/22119/how-can-i-change-the-spacing-before-theorems-with-amsthm
\def\thm@space@setup{%
  \thm@preskip=\parskip \thm@postskip=0pt
}

