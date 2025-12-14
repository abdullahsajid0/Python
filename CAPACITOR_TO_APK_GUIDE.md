# Complete Guide: Convert Any React/Web App to Android APK using Capacitor

This is a comprehensive guide for converting any React, Vite, or web-based project into a signed Android APK using Capacitor. This guide covers all steps, common errors, and their solutions.

---

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Complete Step-by-Step Guide](#complete-step-by-step-guide)
3. [Common Errors and Solutions](#common-errors-and-solutions)
4. [Quick Reference Commands](#quick-reference-commands)
5. [Keystore Management](#keystore-management)
6. [Troubleshooting](#troubleshooting)

---

## Prerequisites

Before starting, ensure you have:

- **Node.js & npm** - [Download](https://nodejs.org/)
- **Android Studio** - [Download](https://developer.android.com/studio)
- **Java Development Kit (JDK)** - Bundled with Android Studio
- **Android SDK** - Automatically installed with Android Studio
- **At least 5GB free disk space**

### Verify Prerequisites:

```powershell
# Check Node version
node --version
npm --version

# Check if Android Studio is installed
Test-Path "C:\Program Files\Android\Android Studio"

# Check if Android SDK is installed
Test-Path "$env:LOCALAPPDATA\Android\Sdk"
```

---

## Complete Step-by-Step Guide

### Step 1: Navigate to Your Project

```powershell
cd C:\path\to\your\project
```

Replace `C:\path\to\your\project` with your actual project path.

---

### Step 2: Install Capacitor and Dependencies

Install Capacitor core, CLI, and Android platform:

```powershell
npm install @capacitor/core @capacitor/cli @capacitor/android --legacy-peer-deps
```

**Why `--legacy-peer-deps`?**
- Capacitor may have peer dependency conflicts with your current packages
- This flag allows installation despite version mismatches
- It won't break anything; Capacitor is well-tested with various versions

---

### Step 3: Initialize Capacitor

Initialize Capacitor configuration:

```powershell
npx cap init
```

You'll be prompted for:

```
✓ What is the name of your app?
  Enter: Your App Name (e.g., "My Awesome App")

✓ What should be the Package ID for your app?
  Enter: com.yourcompany.appname
  
  Example: com.agroreef.app
```

**Package ID Rules:**
- Must be in reverse domain notation: `com.company.appname`
- Lowercase letters, numbers, and dots only
- No spaces or special characters
- Will be unique identifier on Google Play Store

This creates `capacitor.config.ts` in your project root.

---

### Step 4: Build Your Web App

Build the project for production:

```powershell
npm run build
```

This command:
- Compiles your React/Vue/Angular code
- Optimizes assets
- Creates a `dist/` folder with production files
- Takes 1-5 minutes depending on project size

**Expected output:**
```
✓ 1000+ modules transformed
dist/index.html    1.5 kB
dist/assets/...    XXX kB
✓ built in XX.XXs
```

---

### Step 5: Add Android Platform

Add the Android platform to your Capacitor project:

```powershell
npx cap add android
```

This command:
- Creates an `android/` folder with native Android project
- Sets up Gradle configuration
- Prepares for web asset syncing

**Expected output:**
```
✓ Adding native android project in android in XXXms
✓ add in XXXms
[success] android platform added!
```

---

### Step 6: Sync Web App to Android

Copy your web app assets to the Android project:

```powershell
npx cap sync android
```

This command:
- Copies files from `dist/` to Android's asset folder
- Updates Capacitor configuration
- Syncs plugins if any are installed

**Expected output:**
```
✓ Copying web assets from dist to android...
✓ Creating capacitor.config.json in android...
[success] Sync finished
```

---

### Step 7: Configure Java Environment

Set the JAVA_HOME environment variable:

```powershell
$env:JAVA_HOME = "C:\Program Files\Android\Android Studio\jbr"
```

**What is JBR?**
- JBR = JetBrains Runtime
- Bundled with Android Studio
- Contains all Java tools needed for building

---

### Step 8: Clean Gradle (Optional but Recommended)

Clean the build cache:

```powershell
cd android
.\gradlew.bat clean
cd ..
```

This ensures a fresh build without cached artifacts.

---

### Step 9: Fix AGP Version (If Needed)

If you get an error like:
```
Project is using an incompatible version (AGP 8.13.0) of the Android Gradle plugin. Latest supported version is AGP 8.11.1
```

**Solution:**

Edit `android/build.gradle`:

```groovy
// BEFORE:
classpath 'com.android.tools.build:gradle:8.13.0'

// AFTER:
classpath 'com.android.tools.build:gradle:8.11.1'
```

Then run:
```powershell
cd android
.\gradlew.bat clean
cd ..
```

---

### Step 10: Generate Keystore File

**⚠️ Do this ONLY ONCE! Save the keystore file safely.**

Generate a keystore for signing your APK:

```powershell
$env:JAVA_HOME = "C:\Program Files\Android\Android Studio\jbr"
& "C:\Program Files\Android\Android Studio\jbr\bin\keytool.exe" -genkey -v -keystore myapp.keystore -keyalg RSA -keysize 2048 -validity 10000 -alias myapp -dname "CN=Company,OU=Department,O=Company,L=City,ST=State,C=CountryCode" -storepass mypassword -keypass mypassword
```

**Parameters explained:**
- `-keystore myapp.keystore` - Output filename (customize for your app)
- `-alias myapp` - Alias name (customize for your app)
- `-dname "CN=Company,OU=Department,O=Company,L=City,ST=State,C=CountryCode"` - Your info
  - CN = Your Name
  - OU = Department
  - O = Organization
  - L = City
  - ST = State
  - C = Country Code (US, EG, GB, etc.)
- `-storepass mypassword` - Keystore password (customize)
- `-keypass mypassword` - Key password (customize)
- `-validity 10000` - Valid for ~27 years

**Example:**
```powershell
$env:JAVA_HOME = "C:\Program Files\Android\Android Studio\jbr"
& "C:\Program Files\Android\Android Studio\jbr\bin\keytool.exe" -genkey -v -keystore myapp.keystore -keyalg RSA -keysize 2048 -validity 10000 -alias myapp -dname "CN=John Doe,OU=Development,O=My Company,L=Cairo,ST=Cairo,C=EG" -storepass MySecurePass123 -keypass MySecurePass123
```

**Output should show:**
```
Generating 2,048 bit RSA key pair and self-signed certificate...
Entry type: PrivateKeyEntry
...
[success] Certificate fingerprint (MD5): XX:XX:XX:XX:XX:XX:XX:XX
```

---

### Step 11: Configure Signing in build.gradle

Edit `android/app/build.gradle` and add signing configuration:

**Find the `android {` block and add this:**

```groovy
android {
    namespace = "com.yourcompany.appname"
    compileSdk = rootProject.ext.compileSdkVersion
    defaultConfig {
        applicationId "com.yourcompany.appname"
        minSdkVersion rootProject.ext.minSdkVersion
        targetSdkVersion rootProject.ext.targetSdkVersion
        versionCode 1
        versionName "1.0"
        testInstrumentationRunner "androidx.test.runner.AndroidJUnitRunner"
        aaptOptions {
            ignoreAssetsPattern = '!.svn:!.git:!.ds_store:!*.scc:.*:!CVS:!thumbs.db:!picasa.ini:!*~'
        }
    }
    
    // ADD THIS SECTION:
    signingConfigs {
        release {
            storeFile file('../../myapp.keystore')
            storePassword 'MySecurePass123'
            keyAlias 'myapp'
            keyPassword 'MySecurePass123'
        }
    }
    
    buildTypes {
        release {
            signingConfig signingConfigs.release  // ADD THIS LINE
            minifyEnabled false
            proguardFiles getDefaultProguardFile('proguard-android.txt'), 'proguard-rules.pro'
        }
    }
}
```

**Important notes:**
- Change `myapp.keystore` to your actual keystore filename
- Change passwords to match what you set during keystore creation
- The path `../../` means: go up 2 folders from `android/app/` to project root
- Match the `keyAlias` value from Step 10

---

### Step 12: Build Release APK

Build the signed release APK:

```powershell
$env:JAVA_HOME = "C:\Program Files\Android\Android Studio\jbr"
cd android
.\gradlew.bat assembleRelease
cd ..
```

This process:
- Compiles Java code
- Bundles resources
- Creates DEX files
- Signs the APK
- Takes 2-5 minutes

**Expected output:**
```
> Configure project :app
> Task :app:compileReleaseJavaWithJavac
...
BUILD SUCCESSFUL in Xm Xs
XXX actionable tasks: XXX executed
```

**Output location:**
```
android/app/build/outputs/apk/release/app-release.apk
```

---

### Step 13: Verify APK

Check if the APK was created:

```powershell
Test-Path "android/app/build/outputs/apk/release/app-release.apk"
```

Should return `True`.

---

### Step 14: Install on Device/Emulator (Optional)

To test the APK on a connected Android device or emulator:

```powershell
# First ensure device is connected or emulator is running
adb devices

# Install the APK
adb install -r "android/app/build/outputs/apk/release/app-release.apk"
```

---

## Common Errors and Solutions

### Error 1: "npm error could not determine executable to run"

**Cause:** Capacitor not installed

**Solution:**
```powershell
npm install @capacitor/core @capacitor/cli @capacitor/android --legacy-peer-deps
```

---

### Error 2: "ERESOLVE could not resolve dependency"

**Cause:** Peer dependency conflict (common with React 18 + react-leaflet)

**Solution:** Add `--legacy-peer-deps` flag:
```powershell
npm install --legacy-peer-deps
```

Or when installing Capacitor:
```powershell
npm install @capacitor/core @capacitor/cli @capacitor/android --legacy-peer-deps
```

---

### Error 3: "AGP 8.13.0 is incompatible, use AGP 8.11.1"

**Cause:** Android Gradle Plugin version too new

**Solution:**

Edit `android/build.gradle`:
```groovy
// Change from:
classpath 'com.android.tools.build:gradle:8.13.0'

// To:
classpath 'com.android.tools.build:gradle:8.11.1'
```

Then clean:
```powershell
cd android
.\gradlew.bat clean
cd ..
```

---

### Error 4: "JAVA_HOME is not set"

**Cause:** Java environment not configured

**Solution:**
```powershell
$env:JAVA_HOME = "C:\Program Files\Android\Android Studio\jbr"
```

Or set permanently in Windows:
1. Right-click "This PC" → Properties
2. Click "Advanced system settings"
3. Click "Environment Variables"
4. Click "New" (User variables)
5. Variable name: `JAVA_HOME`
6. Variable value: `C:\Program Files\Android\Android Studio\jbr`
7. Click OK and restart PowerShell

---

### Error 5: "keytool: command not found"

**Cause:** keytool not in PATH

**Solution:** Use full path:
```powershell
$env:JAVA_HOME = "C:\Program Files\Android\Android Studio\jbr"
& "$env:JAVA_HOME\bin\keytool.exe" -genkey -v -keystore myapp.keystore -keyalg RSA -keysize 2048 -validity 10000 -alias myapp -dname "CN=Company,OU=Dept,O=Company,L=City,ST=State,C=CountryCode" -storepass password -keypass password
```

---

### Error 6: "Key pair not generated, alias already exists"

**Cause:** Keystore already exists with that alias

**Solution:** 
- Use a different keystore filename, OR
- Use a different alias name, OR
- Delete the old keystore if you don't need it

---

### Error 7: "Gradle build failed: Could not find app-release.apk"

**Cause:** Build failed silently

**Solution:**
```powershell
$env:JAVA_HOME = "C:\Program Files\Android\Android Studio\jbr"
cd android

# Clean and retry
.\gradlew.bat clean
.\gradlew.bat assembleRelease

cd ..
```

---

### Error 8: "Signing configuration not specified"

**Cause:** Missing signingConfigs in build.gradle

**Solution:** Ensure `signingConfigs` block is added in `android/app/build.gradle` and referenced in buildTypes.release

---

### Error 9: "APK signature is invalid"

**Cause:** Wrong keystore password

**Solution:** Verify passwords match in build.gradle:
```groovy
signingConfigs {
    release {
        storeFile file('../../myapp.keystore')
        storePassword 'CorrectPassword'  // Match what you set
        keyAlias 'myapp'
        keyPassword 'CorrectPassword'    // Match what you set
    }
}
```

---

### Error 10: "Cannot find dist folder"

**Cause:** Web app not built

**Solution:**
```powershell
npm run build
npx cap sync android
```

---

## Quick Reference Commands

### Initial Setup
```powershell
# 1. Install Capacitor
npm install @capacitor/core @capacitor/cli @capacitor/android --legacy-peer-deps

# 2. Initialize
npx cap init

# 3. Build web app
npm run build

# 4. Add Android
npx cap add android

# 5. Sync assets
npx cap sync android
```

### For Each Build (After Code Changes)
```powershell
# 1. Rebuild web app
npm run build

# 2. Sync to Android
npx cap sync android

# 3. Set Java and build APK
$env:JAVA_HOME = "C:\Program Files\Android\Android Studio\jbr"
cd android
.\gradlew.bat assembleRelease
cd ..

# 4. APK ready at:
# android/app/build/outputs/apk/release/app-release.apk
```

### Generate Keystore
```powershell
$env:JAVA_HOME = "C:\Program Files\Android\Android Studio\jbr"
& "C:\Program Files\Android\Android Studio\jbr\bin\keytool.exe" -genkey -v -keystore myapp.keystore -keyalg RSA -keysize 2048 -validity 10000 -alias myapp -dname "CN=Name,OU=Dept,O=Company,L=City,ST=State,C=CountryCode" -storepass password -keypass password
```

### Test on Device
```powershell
adb devices
adb install -r "android/app/build/outputs/apk/release/app-release.apk"
```

---

## Keystore Management

### Creating a Keystore

**One-time process:**
1. Generate keystore (see Step 10 above)
2. Save the keystore file in a SAFE location
3. Store credentials in a password manager

### Using Existing Keystore

If you have an existing keystore:

1. Place it in your project root (or any accessible location)
2. Update build.gradle:
   ```groovy
   storeFile file('../../path/to/existing.keystore')
   storePassword 'existing_password'
   keyAlias 'existing_alias'
   keyPassword 'existing_password'
   ```

### Listing Keystore Info

View what's inside your keystore:

```powershell
$env:JAVA_HOME = "C:\Program Files\Android\Android Studio\jbr"
& "$env:JAVA_HOME\bin\keytool.exe" -list -v -keystore myapp.keystore -storepass password
```

### Important Keystore Rules

⚠️ **CRITICAL:**
- **KEEP THE KEYSTORE FILE SAFE** - You need it to update your app
- **Never lose the password** - You can't recover it
- **Never share the keystore** - It's like your app's signature
- **Use same keystore for updates** - Google Play requires same signing key
- **Back it up** - Store in cloud (encrypted) or external drive

---

## Troubleshooting

### General Troubleshooting Steps

**If anything fails, try this in order:**

```powershell
# 1. Set Java home
$env:JAVA_HOME = "C:\Program Files\Android\Android Studio\jbr"

# 2. Rebuild web app
npm run build

# 3. Sync to Android
npx cap sync android

# 4. Clean Gradle
cd android
.\gradlew.bat clean
cd ..

# 5. Build again
cd android
.\gradlew.bat assembleRelease
cd ..
```

### Check Build Output

If gradle fails, check the detailed error:

```powershell
cd android
.\gradlew.bat assembleRelease --stacktrace
cd ..
```

### Increase Gradle Memory

If you get out-of-memory errors:

Create `android/gradle.properties`:
```properties
org.gradle.jvmargs=-Xmx2048m
```

### Clear npm Cache

If npm install fails:

```powershell
npm cache clean --force
npm install @capacitor/core @capacitor/cli @capacitor/android --legacy-peer-deps
```

### Update Android Tools

If you have old Android SDK tools:

1. Open Android Studio
2. Tools → SDK Manager
3. Update all SDK tools to latest
4. Restart PowerShell

---

## Project Structure After Setup

Your project will look like this:

```
your-project/
├── src/                          (Your React/Vue/Angular code)
├── dist/                         (Built web app - created by npm run build)
├── android/                      (Native Android project - created by npx cap add android)
│   ├── app/
│   │   ├── build/
│   │   │   └── outputs/
│   │   │       └── apk/
│   │   │           └── release/
│   │   │               └── app-release.apk  ← YOUR SIGNED APK
│   │   └── build.gradle          (Edit for signing config)
│   ├── build.gradle              (Edit AGP version if needed)
│   └── gradle/
├── capacitor.config.ts           (Capacitor config - created by npx cap init)
├── myapp.keystore                (Your keystore - created by keytool)
└── package.json
```

---

## FAQ

**Q: Do I need Android Studio?**
A: No, but it's recommended for debugging. You can build from command line alone.

**Q: Can I use this for iOS?**
A: Yes! Use `npx cap add ios` and similar steps.

**Q: Can I share the keystore?**
A: NO! It's like your app's secret key. Keep it safe and never commit to git.

**Q: How often should I rebuild?**
A: Whenever you update your code - just run `npm run build`, `npx cap sync android`, and `gradlew assembleRelease`.

**Q: Can I update the app on Google Play?**
A: Yes! Use the same keystore to sign updates. Google Play requires the same signing key.

**Q: What if I lose my keystore?**
A: You can't update your app on Google Play anymore (for that app ID). Always backup your keystore!

**Q: How long is the APK valid?**
A: As long as you set it (usually 10000 days = 27+ years). The validity date is just for the certificate, not the app itself.

---

## Summary

To convert any web app to Android APK:

1. Install Capacitor packages
2. Initialize Capacitor
3. Build web app
4. Add Android platform
5. Sync assets
6. Fix any errors (AGP version, Java setup)
7. Generate keystore (one-time)
8. Configure signing in build.gradle
9. Build release APK

**That's it!** Your signed APK is ready to distribute.

---

## Additional Resources

- [Capacitor Documentation](https://capacitorjs.com/docs)
- [Android Gradle Plugin Docs](https://developer.android.com/studio/releases/gradle-plugin)
- [Android App Signing](https://developer.android.com/studio/publish/app-signing)
- [Google Play Console](https://play.google.com/console)

---

## Version History

- **v1.0** - December 14, 2025 - Initial comprehensive guide
