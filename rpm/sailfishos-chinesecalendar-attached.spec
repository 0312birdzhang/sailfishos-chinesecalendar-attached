# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       sailfishos-chinesecalendar-attached

# >> macros
BuildArch: armv7hl
# << macros

Summary:    Chinese Calendar patch
Version:    0.0.2
Release:    1
Group:      Qt/Qt
License:    TODO
Source0:    %{name}-%{version}.tar.bz2
Requires:   patchmanager
Requires:   jolla-calendar >= 0.4.39
%description
Add Chinese calendar to Jolla Calendar.


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre



# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
mkdir -p %{buildroot}/usr/share/patchmanager/patches/sailfishos-chinesecalendar-attached
cp -r patch/* %{buildroot}/usr/share/patchmanager/patches/sailfishos-chinesecalendar-attached
mkdir -p %{buildroot}/usr/share/jolla-calendar/pages
cp patch/GetCNDate.js %{buildroot}/usr/share/jolla-calendar/pages
# << install pre

# >> install post
# << install post

%pre
# >> pre
if [ -f /usr/sbin/patchmanager ]; then
/usr/sbin/patchmanager -u sailfishos-chinesecalendar-attached || true
fi
# << pre

%preun
# >> preun
if [ -f /usr/sbin/patchmanager ]; then
/usr/sbin/patchmanager -u sailfishos-chinesecalendar-attached || true
fi
# << preun

%files
%defattr(-,root,root,-)
%{_datadir}/patchmanager/patches/sailfishos-chinesecalendar-attached
%{_datadir}/jolla-calendar/pages
# >> files
# << files
