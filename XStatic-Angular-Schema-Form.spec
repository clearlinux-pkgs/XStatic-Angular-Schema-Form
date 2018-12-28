#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : XStatic-Angular-Schema-Form
Version  : 0.8.13.0
Release  : 2
URL      : https://files.pythonhosted.org/packages/57/71/ceea2c0a72e2ee2d316d6ab1c06b21faa9f5cbc4b36a4127d7847b7079c5/XStatic-Angular-Schema-Form-0.8.13.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/57/71/ceea2c0a72e2ee2d316d6ab1c06b21faa9f5cbc4b36a4127d7847b7079c5/XStatic-Angular-Schema-Form-0.8.13.0.tar.gz
Summary  : Angular-Schema-Form 0.8.13 (XStatic packaging standard)
Group    : Development/Tools
License  : MIT
Requires: XStatic-Angular-Schema-Form-python3
Requires: XStatic-Angular-Schema-Form-python
BuildRequires : buildreq-distutils3

%description
---------------
        
        Angular JavaScript library packaged for setuptools (easy_install) / pip.
        
        This package is intended to be used by **any** project that needs these files.
        
        It intentionally does **not** provide any extra code except some metadata
        **nor** has any extra requirements. You MAY use some minimal support code from
        the XStatic base package, if you like.
        
        You can find more info about the xstatic packaging way in the package `XStatic`.

%package python
Summary: python components for the XStatic-Angular-Schema-Form package.
Group: Default
Requires: XStatic-Angular-Schema-Form-python3
Provides: xstatic-angular-schema-form-python

%description python
python components for the XStatic-Angular-Schema-Form package.


%package python3
Summary: python3 components for the XStatic-Angular-Schema-Form package.
Group: Default
Requires: python3-core

%description python3
python3 components for the XStatic-Angular-Schema-Form package.


%prep
%setup -q -n XStatic-Angular-Schema-Form-0.8.13.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1533916244
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
