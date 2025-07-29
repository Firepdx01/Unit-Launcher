from modrith_manager import ModrithManager, Profile

async def main():
    # Create a ModrithManager instance
    manager = ModrithManager()

    # Create a profile
    profile = Profile(name="MyProfile", game_version="1.16.5", mod_loader="Forge", mods=["mod1.jar", "mod2.jar"])
    
    # Save profile
    manager.save_profile(profile)
    
    # Load profile
    loaded_profile = manager.load_profile("MyProfile")
    print(loaded_profile.name, loaded_profile.game_version)
    
    # List profiles
    profiles = manager.list_profiles()
    print(profiles)
    
    # List mods
    mods = manager.list_mods()
    print(mods)
    
    # Cleanup
    manager.close()

if __name__ == "__main__":
    asyncio.run(main())
