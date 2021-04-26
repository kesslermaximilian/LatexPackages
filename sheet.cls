\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{sheet}[2021/03/31 Exercise-Sheet-Class by Maximilian Kessler (private use)]

\RequirePackage{scrbase}

\newif\iflargename\largenamefalse
\DeclareOption{large-name}{\largenametrue}
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{scrartcl}}
\ProcessOptions\relax

\LoadClass{scrartcl}

\KOMAoption{fontsize}{12pt}
\KOMAoption{parskip}{half-}
\KOMAoption{DIV}{12}
\KOMAoption{headings}{normal}

\RequirePackage{mymath}
\RequirePackage{scrlayer-scrpage}
\RequirePackage{subfig}
\RequirePackage[shortlabels]{enumitem}
%\RequirePackage[hidelinks]{hyperref}
\RequirePackage{graphicx}
\RequirePackage{ifplatform}
\graphicspath{{./out/graphics/}}

\KOMAoption{headsepline}{:}

\AtBeginDocument{\maketitle}

\def\@course{}%
\DeclareRobustCommand*{\course}[1]{\gdef\@course{#1}}
\def\@sheetnumber{}%
\DeclareRobustCommand*{\sheetnumber}[1]{\gdef\@sheetnumber{\ifenglish Sheet #1 \else Übungsblatt #1\fi}}

\renewcommand*{\@date}{\today}

\renewcommand*{\maketitle}{
	\thispagestyle{plain}
	{\makebox[0pt][l]{\usekomafont{myauthor}\@author}\hfill\makebox[0pt][r]{\usekomafont{date}\@date}\par}
	\vspace{0.5em}
	{\centering\usekomafont{title}\@course\par}
    {\centering\usekomafont{subtitle}\@sheetnumber \par}
	\vspace{2em}
	\hrule
	\addvspace{2em}
}

\setkomafont{title}{\LARGE\bfseries}
\setkomafont{subtitle}{}
\newkomafont{myauthor}{}
\setkomafont{date}{}
\newkomafont{headtitle}{\itshape}
\setkomafont{pageheadfoot}{\footnotesize}
\setkomafont{descriptionlabel}{\bfseries}
\setkomafont{pagenumber}{\normalsize}

\pagestyle{scrheadings}
\ihead[]{\iflargename \usekomafont{myauthor}\@author \\ \@course\;- \@sheetnumber\else \usekomafont{myauthor}\@author\fi }
\chead[]{\iflargename \else \usekomafont{subtitle}\@course\;- \@sheetnumber\fi}
\ohead[]{\usekomafont{date}\@date}

\allowdisplaybreaks[1]

% Page layout
\setlength{\parindent}{0pt}

\RequirePackage{geometry}
\geometry{a4paper, left=2cm, right=2cm, top=3cm-15pt, bottom=3cm-15pt,  head=15.0pt, headsep=10pt}

\setlength{\skip\footins}{15pt}

\setlength{\abovecaptionskip}{0cm}
\setlength{\belowcaptionskip}{0cm}

%Für Zeilenabstand 1,5
\RequirePackage[onehalfspacing]{setspace}
