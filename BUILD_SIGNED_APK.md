# Build Signed APK Guide for AgroReef AI

This guide contains all the steps and commands needed to build a signed APK for the AgroReef AI app. Follow these steps in order.

## Prerequisites

- Node.js and npm installed
- Android Studio installed (includes JDK)
- A terminal/PowerShell window

---

## Step 1: Install Capacitor and Android Platform

Install Capacitor packages with legacy peer dependencies flag:

```powershell
cd D:\agroreef-ai-main
npm install @capacitor/core @capacitor/cli @capacitor/android --legacy-peer-deps
```

---

## Step 2: Initialize Capacitor

Initialize Capacitor with your app details:

```powershell
npx cap init
```

When prompted, enter:
- **App name:** AgroReef ai
- **Package ID:** com.agroreef.app

---

## Step 3: Add Android Platform

Add the Android platform to your project:

```powershell
npx cap add android
```

---

## Step 4: Build Web App

Build the web application for production:

```powershell
npm run build
```

This creates the `dist/` folder with your web assets.

---

## Step 5: Sync Web App to Android

Sync the built web app to the Android project:

```powershell
npx cap sync android
```

---

## Step 6: Fix Android Gradle Plugin Version (if needed)

If you get an error about incompatible AGP version, update the Gradle plugin:

Edit `android/build.gradle` and change the dependency from:
```groovy
classpath 'com.android.tools.build:gradle:8.13.0'
```

to:
```groovy
classpath 'com.android.tools.build:gradle:8.11.1'
```

---

## Step 7: Set JAVA_HOME and Clean Gradle

Set the JAVA_HOME environment variable to Android Studio's bundled JDK and clean:

```powershell
$env:JAVA_HOME = "C:\Program Files\Android\Android Studio\jbr"
cd D:\agroreef-ai-main\android
.\gradlew.bat clean
```

---

## Step 8: Generate Keystore (One-time only)

Generate a keystore file for signing APKs. **Only do this once** - keep the keystore file safe for future updates:

```powershell
$env:JAVA_HOME = "C:\Program Files\Android\Android Studio\jbr"
cd D:\agroreef-ai-main
& "C:\Program Files\Android\Android Studio\jbr\bin\keytool.exe" -genkey -v -keystore agroreef.keystore -keyalg RSA -keysize 2048 -validity 10000 -alias agroreef -dname "CN=AgroReef,OU=AgroReef,O=AgroReef,L=Egypt,ST=Cairo,C=EG" -storepass agroreef123 -keypass agroreef123
```

**Keystore Details:**
- File: `agroreef.keystore`
- Store Password: `agroreef123`
- Key Alias: `agroreef`
- Key Password: `agroreef123`

---

## Step 9: Configure Signing in build.gradle

Update `android/app/build.gradle` to add signing configuration.

Find the `android {` section and add the signing config:

```groovy
android {
    namespace = "com.agroreef.app"
    compileSdk = rootProject.ext.compileSdkVersion
    defaultConfig {
        applicationId "com.agroreef.app"
        minSdkVersion rootProject.ext.minSdkVersion
        targetSdkVersion rootProject.ext.targetSdkVersion
        versionCode 1
        versionName "1.0"
        testInstrumentationRunner "androidx.test.runner.AndroidJUnitRunner"
        aaptOptions {
             // Files and dirs to omit from the packaged assets dir, modified to accommodate modern web apps.
             // Default: https://android.googlesource.com/platform/frameworks/base/+/282e181b58cf72b6ca770dc7ca5f91f135444502/tools/aapt/AaptAssets.cpp#61
            ignoreAssetsPattern = '!.svn:!.git:!.ds_store:!*.scc:.*:!CVS:!thumbs.db:!picasa.ini:!*~'
        }
    }
    signingConfigs {
        release {
            storeFile file('../../agroreef.keystore')
            storePassword 'agroreef123'
            keyAlias 'agroreef'
            keyPassword 'agroreef123'
        }
    }
    buildTypes {
        release {
            signingConfig signingConfigs.release
            minifyEnabled false
            proguardFiles getDefaultProguardFile('proguard-android.txt'), 'proguard-rules.pro'
        }
    }
}
```

---

## Step 10: Build Signed Release APK

Build the signed release APK:

```powershell
$env:JAVA_HOME = "C:\Program Files\Android\Android Studio\jbr"
cd D:\agroreef-ai-main\android
.\gradlew.bat assembleRelease
```

The APK will be created at:
```
D:\agroreef-ai-main\android\app\build\outputs\apk\release\app-release.apk
```

---

## Step 11: Install APK on Device (Optional)

To install the APK on a connected Android device or emulator:

```powershell
adb install -r "D:\agroreef-ai-main\android\app\build\outputs\apk\release\app-release.apk"
```

---

## Quick Commands Summary

For future builds, after making code changes, run these commands in order:

```powershell
# 1. Build web app
npm run build

# 2. Sync to Android
npx cap sync android

# 3. Set Java home and build signed APK
$env:JAVA_HOME = "C:\Program Files\Android\Android Studio\jbr"
cd D:\agroreef-ai-main\android
.\gradlew.bat assembleRelease

# 4. APK location
# D:\agroreef-ai-main\android\app\build\outputs\apk\release\app-release.apk
```

---

## Important Notes

⚠️ **Keep the keystore file safe!**
- Store `agroreef.keystore` in a secure location
- You'll need this file and the password to update the app in the future
- Never commit it to public repositories

✅ **File Locations:**
- Signed APK: `android/app/build/outputs/apk/release/app-release.apk`
- Keystore: `agroreef.keystore` (in project root)
- Build config: `android/app/build.gradle`

🔄 **For Updates:**
When you want to rebuild the app:
1. Update your code
2. Run `npm run build`
3. Run `npx cap sync android`
4. Set JAVA_HOME and run `.\gradlew.bat assembleRelease`

---

## Troubleshooting

**If gradle fails:**
```powershell
$env:JAVA_HOME = "C:\Program Files\Android\Android Studio\jbr"
.\gradlew.bat clean
.\gradlew.bat assembleRelease
```

**If you get signing errors:**
- Verify `agroreef.keystore` exists in project root
- Check that paths in `build.gradle` are correct (should be `../../agroreef.keystore`)
- Verify passwords match (both are `agroreef123`)

**If peer dependency errors appear:**
- Always use `--legacy-peer-deps` flag when installing packages

---

## Keystore Credentials

**IMPORTANT: Save these credentials in a safe place!**

- **Keystore File:** agroreef.keystore
- **Store Password:** agroreef123
- **Key Alias:** agroreef
- **Key Password:** agroreef123
- **Validity:** 10000 days (27+ years)

---

## Created Date

December 14, 2025

## Last Updated

December 14, 2025
