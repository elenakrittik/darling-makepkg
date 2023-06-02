# Maintainer: Elena Krittik <elenakrittik@gmail.com>

pkgname=darling-edge-bin
pkgver=894d62c91d78d56e05708f40f2d7e490fce5f046
pkgdesc="Darwin/macOS emulation layer for Linux"
arch=("x86_64")
url="https://github.com/darlinghq/darling"
license=('GPL')
groups=('darling-bin')
provides=('darling')
conflicts=('darling' 'darling-git')
depends=('dbus>=1.9.14' 'ffmpeg>=2:4.0' 'freetype2>=2.2.1' 'fuse2>=2.2' 'giflib>=5.1'
         'glibc>=2.14' 'glu' 'libgl' 'libglvnd' 'libjpeg-turbo>=2.0' 'libpulse>=0.99.1'
         'libtiff>=4.0.3' 'libx11' 'libxcursor>1.1.2' 'libxext' 'libxkbfile>=1.1.0'
         'libxrandr')
source=("https://github.com/darlinghq/darling/suites/13105150970/artifacts/711636327")
options=('!strip')
install=$pkgname.install
makedepends=()
optdepends=()
replaces=()
backup=()
changelog=""
noextract=()
md5sums=()

package() {
  # Extract package data
  cd "$pkgdir"
  tar xf "$srcdir/data.tar.xz"

  install -Dm644 \
    usr/libexec/darling/System/Library/Frameworks/Ruby.framework/Versions/2.6/usr/share/ri/2.6.0/system/Gem/SpecificationPolicy/validate_licenses-i.ri \
    usr/share/licenses/$pkgname/LICENSE

  install -Dm644 usr/share/doc/darling/copyright \
    usr/share/licenses/$pkgname/COPYRIGHT
}

