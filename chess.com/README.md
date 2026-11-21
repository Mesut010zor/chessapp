# Chess.com masaüstü başlatıcısı

Uygulamalar menüsünden **Chess.com** öğesini seç veya `/home/mesut/vscode/chess.com/chess-desktop` çalıştır. Chromium, Chrome veya Brave gerektirir. Root yetkisi gerekmez.

Bu bağımsız bir satranç motoru veya resmî bir Chess.com ürünü değildir. Başlatıcı doğrudan `https://www.chess.com/tr` adresini uygulama penceresinde gösterir. Arayüz siteden gelir ve internet gerektirir. Hesabına giriş yapmak istersen normal tarayıcından ayrı olarak bir kez giriş yapman gerekir. Çerezler ve ayarlar `${XDG_CONFIG_HOME:-$HOME/.config}/chess-com-desktop` dizininde kalır.

Menü kısayolunu kaldırmak için `${XDG_DATA_HOME:-$HOME/.local/share}/applications/chess-com-desktop.desktop` dosyasını sil. Bu işlem oturumu silmez. Proje klasörünü taşırsan kısayolun `Exec` ve `Icon` yollarını güncelle.
