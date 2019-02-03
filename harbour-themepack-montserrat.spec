Name:          harbour-themepack-montserrat
Version:       0.0.1
Release:       1
Summary:       Montserrat theme pack
Obsoletes:     harbour-iconpacksupport <= 0.0.4-4
Conflicts:     harbour-iconpacksupport
Group:         System/Tools
Vendor:        fravaccaro
Distribution:  SailfishOS
Requires:      harbour-themepacksupport >= 0.0.7-2
Packager:      fravaccaro <fravaccaro@jollacommunity.it>
URL:           www.jollacommunity.it
License:       GPLv3

%description
Montserrat font package for Theme pack support for Sailfish OS.

%files
%defattr(-,root,root,-)
/usr/share/*

%postun
if [ $1 = 0 ]; then
    // Do stuff specific to uninstalls
rm -rf /usr/share/harbour-themepack-%{name}
else
if [ $1 = 1 ]; then
    // Do stuff specific to upgrades
echo "Upgrading"
fi
fi

%changelog
* Mon Feb 4 2019 0.0.1
- First build.
