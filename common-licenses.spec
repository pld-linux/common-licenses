Summary:	Common software licenses
Summary(de.UTF-8):	Populär Programmlizenzen
Summary(eo.UTF-8):	Popularaj licencoj programaj
Summary(es.UTF-8):	Populares licencias del software
Summary(it.UTF-8):	Popolare lizence dei programme
Summary(pl.UTF-8):	Popularne licencje oprogramowania
Summary(ru.UTF-8):	Популярные лицензие програм
Name:		common-licenses
Version:	1.1
Release:	2
License:	none
Group:		Documentation
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	28782b4d7d610942994f4e0620127b4e
Source1:	ZPL.tar.gz
URL:		http://www.gnu.org/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains common licenses - GPL, LGPL, FDL and some others
with some available unofficial (there are no official) translations.
See also http://www.gnu.org/licenses/license-list.html and
http://www.opensource.org/licenses/.

%description -l pl.UTF-8
Pakiet zawiera popularne licencje - GPL, LGPL, FDL oraz kilka innych
wraz z dostępnymi nieoficjalnymi (oficjalnych brak) tłumaczeniami.
Spójrz również na http://www.gnu.org/licenses/license-list.html oraz
http://www.opensource.org/licenses/.

%prep
%setup -q -a1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.{html,txt}
%doc %lang(bg) bg_BG Bulgarian
%doc %lang(cs) cs_CZ Czech
%doc %lang(ca) ca_ES Catalan
%doc %lang(de) de_DE Deutsche
%doc %lang(el) el_GR Greek
%doc %lang(eo) eo Esperanto
%doc %lang(es) es_ES Spanish
%doc %lang(fr) fr_FR French
%doc %lang(gl) gl_ES Galician
%doc %lang(he) he_IL Hebrew
%doc %lang(id) id_ID Indonesian
%doc %lang(it) it_IT Italian
%doc %lang(ja) ja_JP Japan
%doc %lang(ka) ka_GE Georgian
%doc %lang(ko) ko_KR Korean
%doc %lang(nl) nl_NL Dutch
%doc %lang(pl) pl_PL Polish
%doc %lang(pt) pt_BR Brazilian\ portuguese
%doc %lang(ru) ru_RU Russian
%doc %lang(ro) ro_RO Romanian
%doc %lang(sv) sv_SE Swedish
%doc %lang(th) th_TH Thai
%doc %lang(tr) tr_TR Turkish
%doc %lang(uk) uk_UA Ukrainian
